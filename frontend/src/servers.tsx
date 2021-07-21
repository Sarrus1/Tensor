import React, { useState, useEffect, useRef } from "react";
import { render } from "react-dom";
import { Modal, Button } from "react-bootstrap";
import axios from "axios";
import { Line } from "react-chartjs-2";
import { v4 as uuidv4 } from "uuid";
import Ansi from "ansi-to-react";
import { registry } from "chart.js";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

interface serverInfo {
  serverName: string;
  maxPlayer: number;
  connectionInfo: string;
  currentMap: number;
  currentPlayers: number;
  labels: string[];
  data: number[];
  port: number[];
}

interface buttonAttributes {
  variant: string;
  name: string;
}

interface serverCommandStatus {
  timestamp: string;
  output: string;
}

type commandType = "1" | "2" | "3" | "4";

function NewlineText(props): JSX.Element {
  const text = props.text;
  const newText = text.split("\n").map((str) => (
    <p>
      <Ansi>{str}</Ansi>
    </p>
  ));

  return newText;
}

function getAttributes(command: commandType): buttonAttributes {
  switch (command) {
    case "1":
      return { variant: "success", name: "Start" };
    case "2":
      return { variant: "danger", name: "Stop" };
    case "3":
      return { variant: "info", name: "Restart" };
    case "4":
      return { variant: "warning", name: "Update" };
  }
}

function ControlButtons(props): JSX.Element {
  const server: serverInfo = props.server;
  const command: commandType = props.command;

  const [modalText, setModalText] = useState("");
  const [showModal, setshowModal] = useState(false);

  const handleCloseModal = () => {
    setModalText("");
    setshowModal(false)
  };
  const handleShowModal = () => setshowModal(true);

  if (!canControl) {
    return <div />;
  }
  return (
    <>
      <Modal show={showModal} onHide={handleCloseModal}>
        <Modal.Header closeButton>
          <Modal.Title>Server status</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <NewlineText text={modalText} />
        </Modal.Body>
      </Modal>
      <div className="col-md-3 mt-2">
        <Button
           style={{width:"100%"}}
          variant={getAttributes(command).variant}
          onClick={() => {
            const uuid = uuidv4();
            axios
              .post(
                `/api/servers/servers-control/`,
                {
                  uuid: uuid,
                  port: server.port,
                  command: command,
                },
                {
                  headers: {
                    "Content-Type": "application/json",
                  },
                }
              )
              .then((res) => {
                handleShowModal();
                setModalText("Sending command...");
                const interval = setInterval(() => {
                  axios
                    .get("/api/servers/servers-control/", {
                      params: {
                        uuid: uuid,
                      },
                    })
                    .then((res) => {
                      let data: serverCommandStatus = res.data;
                      if (data.output != "NULL_RESPONSE") {
                        setModalText(data.output);
                        return;
                      }
                      clearInterval(interval);
                    })
                    .catch((err) => {
                      console.log(err);
                      clearInterval(interval);
                    });
                }, 1000);
              })
              .catch((err) => {
                console.log(err);
              });
          }}
        >
          {getAttributes(command).name}
        </Button>
      </div>
    </>
  );
}

function ServerCard(props): JSX.Element {
  const server: serverInfo = props.server;

  return (
    <div className="row">
      <div className="col-md-12">
        <div className="card card-primary">
          <div className="card-header">
            <h3 className="card-title">{server.serverName}</h3>
          </div>
          <div className="card-body">
            <div className="row">
              <div className="col-md-4">
                <table className="table table">
                  <tbody>
                    <tr>
                      <td>Players</td>
                      <td>{`${server.currentPlayers}/${server.maxPlayer}`}</td>
                    </tr>
                    <tr>
                      <td>Current map</td>
                      <td>{server.currentMap}</td>
                    </tr>
                    <tr>
                      <td>IP</td>
                      <td>{server.connectionInfo}</td>
                    </tr>
                  </tbody>
                </table>
                <a
                  type="button"
                  href={`steam://connect/${server.connectionInfo}`}
                  className="btn btn-block btn-info"
                >
                  Join
                </a>
              </div>
              <div className="col-md-2 mt-3">
                <img
                  src={`https://image.gametracker.com/images/maps/160x120/csgo/${server.currentMap}.jpg`}
                  className="rounded mx-auto d-block"
                />
              </div>
              <div className="col-md-6">
                <ServerChart server={server} />
              </div>
            </div>
            <div className="row">
              <ControlButtons server={server} command="1" />
              <ControlButtons server={server} command="2" />
              <ControlButtons server={server} command="3" />
              <ControlButtons server={server} command="4" />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function ServerChart(props): JSX.Element {
  const server: serverInfo = props.server;
  const data = {
    labels: server.labels,
    datasets: [
      {
        data: server.data,
        label: "",
        fill: true,
        lineTension: 0.4,
        backgroundColor: "rgba(60,141,188,0.9)",
        borderColor: "rgba(60,141,188,0.8)",
        pointRadius: 1,
        pointColor: "#3b8bba",
        pointStrokeColor: "rgba(60,141,188,1)",
        pointHighlightFill: "#fff",
        pointHighlightStroke: "rgba(60,141,188,1)",
      },
    ],
  };
  let options = {
    maintainAspectRatio: false,
    responsive: true,
    plugins: {
      legend: {
        display: false,
      },
      tooltip: {
        mode: "index",
        intersect: false,
      },
      hover: {
        mode: "nearest",
        intersect: true,
      },
    },
    scales: {
      x: {
        grid: {
          display: false,
        },
      },
      y: {
        grid: {
          display: false,
        },
        min: 0,
        max: server.maxPlayer,
      },
    },
  };

  return <Line data={data} options={options} type="line" />;
}

function App(props): JSX.Element {
  const [servers, setServers] = useState<serverInfo[]>([]);

  useEffect(() => {
    axios.get(`/api/servers/playercount/`).then((res) => {
      setServers(res.data);
    });
  }, []);
  const cards = [];
  let i = 0;
  for (let server of servers) {
    cards.push(<ServerCard key={i++} server={server} />);
  }
  return <div>{cards}</div>;
}

render(<App />, document.getElementById("root"));
