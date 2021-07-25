import React, { useState } from "react";
import { render } from "react-dom";
import axios, { AxiosResponse, AxiosError } from "axios";
import { TextField, Select, Snackbar, LinearProgress } from "@material-ui/core";
import { Alert } from "@material-ui/lab";
import { Button, Modal } from "react-bootstrap";
var dayjs = require("dayjs");
var customParseFormat = require("dayjs/plugin/customParseFormat");

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

function App(props): JSX.Element {
	const [searchEnd, setSearchEnd] = useState(false);
	const [found, setFound] = useState(false);
	const [serverName, setServerName] = useState("");
	const [playerName, setPlayerName] = useState("");
  const [banDetailsData, setBanDetailsData] = useState({});
	const [steamID, setSteamID] = useState("");
  const [customReason, setCustomReason] = useState(false);
  const [alertMessage, setAlertMessage] = useState({
    message: "",
    severity: "",
  });

  const [helperText, setHelperText] = useState("");

	const [showSearch, setShowSearch] = useState(false);
	const handleCloseSearch = () => {
		setShowSearch(false);
		setFound(false);
		setServerName("");
		setPlayerName("");
	}
  const handleShowSearch = () => setShowSearch(true);

  const formGroup: React.CSSProperties = {
    marginBottom: "1rem",
  };

  const fieldStyle: React.CSSProperties = {
    width: "100%",
  };

  return (
    <>
      <Snackbar
        open={alertMessage.message != ""}
        autoHideDuration={6000}
        onClose={() => setAlertMessage({ ...alertMessage, message: "" })}
        anchorOrigin={{ vertical: "bottom", horizontal: "right" }}
      >
        <Alert
          onClose={() => setAlertMessage({ ...alertMessage, message: "" })}
          severity={alertMessage.severity}
          variant="filled"
        >
          {alertMessage.message}
        </Alert>
      </Snackbar>
      <form
        id="edit-form"
        onSubmit={(event) => {
          event.preventDefault();
        }}
      >
        <fieldset style={formGroup}>
          <label>Steam ID</label>
          <TextField
            error={helperText != ""}
            label=""
            variant="outlined"
            size="small"
            style={fieldStyle}
            helperText={helperText}
            onChange={(event) => {
              let newDetailsData = banDetailsData;
              newDetailsData["steamid"] = event.target.value;
              setBanDetailsData(newDetailsData);
            }}
          />
        </fieldset>

        <fieldset style={formGroup}>
          <label>Reason</label>
          <Select
            native
            labelId="reason-label"
            id="reason"
            style={fieldStyle}
            onChange={(event) => {
              let newDetailsData = banDetailsData;
              newDetailsData["reason"] = event.target.value;
              setBanDetailsData(newDetailsData);
              setCustomReason(newDetailsData["reason"] === "other");
            }}
          >
            <option value="" selected="">
              {" "}
              -- Select Reason --{" "}
            </option>
            <optgroup label="Hacking">
              <option value="Aimbot">Aimbot</option>
              <option value="Antirecoil">Antirecoil</option>
              <option value="Wallhack">Wallhack</option>
              <option value="Spinhack">Spinhack</option>
              <option value="Multi-Hack">Multi-Hack</option>
              <option value="No Smoke">No Smoke</option>
              <option value="No Flash">No Flash</option>
            </optgroup>
            <optgroup label="Behavior">
              <option value="Team Killing">Team Killing</option>
              <option value="Team Flashing">Team Flashing</option>
              <option value="Spamming Mic/Chat">Spamming Mic/Chat</option>
              <option value="Inappropriate Spray">Inappropriate Spray</option>
              <option value="Inappropriate Language">
                Inappropriate Language
              </option>
              <option value="Inappropriate Name">Inappropriate Name</option>
              <option value="Ignoring Admins">Ignoring Admins</option>
              <option value="Team Stacking">Team Stacking</option>
            </optgroup>
            <option value="other">Other Reason</option>
          </Select>
        </fieldset>

        <fieldset style={formGroup}>
          <label>Ban Length</label>
          <TextField
            label=""
            variant="outlined"
            multiline
            rows={2}
            rowsMax={5}
            defaultValue=""
            style={{
              display: customReason ? "block" : "none",
              ...fieldStyle,
            }}
            onChange={(event) => {
              let newDetailsData = banDetailsData;
              newDetailsData["reason"] = event.target.value;
              setBanDetailsData(newDetailsData);
            }}
          />
          <Select
            native
            labelId="banlength-label"
            id="banlength"
            style={fieldStyle}
            onChange={(event) => {
              let newDetailsData = banDetailsData;
              newDetailsData["reason"] = event.target.value;
              setBanDetailsData(newDetailsData);
              dayjs.extend(customParseFormat);
              let endDate: number;
              let length: number = event.target.value as number;
              if ((length as unknown as string) === "0") {
                endDate = 0;
              } else {
                endDate = dayjs()
                  .add(length as unknown as string, "minute")
                  .unix();
              }
              newDetailsData["ends"] = endDate as number;
              newDetailsData["length"] = (length * 60) as number;
              setBanDetailsData(newDetailsData);
            }}
          >
            <option value="" selected="">
              {" "}
              -- Ban Length --{" "}
            </option>
            <option value="0">Permanent</option>
            <optgroup label="minutes">
              <option value="1">1 minute</option>
              <option value="5">5 minutes</option>
              <option value="10">10 minutes</option>
              <option value="15">15 minutes</option>
              <option value="30">30 minutes</option>
              <option value="45">45 minutes</option>
            </optgroup>
            <optgroup label="hours">
              <option value="60">1 hour</option>
              <option value="120">2 hours</option>
              <option value="180">3 hours</option>
              <option value="240">4 hours</option>
              <option value="480">8 hours</option>
              <option value="720">12 hours</option>
            </optgroup>
            <optgroup label="days">
              <option value="1440">1 day</option>
              <option value="2880">2 days</option>
              <option value="4320">3 days</option>
              <option value="5760">4 days</option>
              <option value="7200">5 days</option>
              <option value="8640">6 days</option>
            </optgroup>
            <optgroup label="weeks">
              <option value="10080">1 week</option>
              <option value="20160">2 weeks</option>
              <option value="30240">3 weeks</option>
            </optgroup>
            <optgroup label="months">
              <option value="43200">1 month</option>
              <option value="86400">2 months</option>
              <option value="129600">3 months</option>
              <option value="259200">6 months</option>
              <option value="518400">12 months</option>
            </optgroup>
          </Select>
        </fieldset>
      </form>
      <Button
        style={{ margin: "0.25rem" }}
        variant="success"
        type="submit"
        name="submit"
        form="edit-form"
        onClick={() => {
          axios
            .post(`/api/bans/`, banDetailsData, {
              headers: {
                "Content-Type": "application/json",
              },
            })
            .then((response: AxiosResponse) => {
							let name: string = response.data.name;
							setPlayerName(name);
							setSteamID(response.data.steamid);
              setAlertMessage({
                message: `Added a ban for ${name}.`,
                severity: "success",
              });
							setShowSearch(true);
							axios.get(`/api/bans/kick-from-server/?steamid=${steamID}`)
							.then((response: AxiosResponse) => {
								setSearchEnd(true);
								if (response.data.found === "true"){
									setFound(true);
									setServerName(response.data.server);
								}
								else{
									setFound(false);
									setServerName("NOT_FOUND");
								}
							})
            })
            .catch((reason: AxiosError) => {
              if (reason.response!.status === 403) {
                setAlertMessage({
                  message: `Permission denied`,
                  severity: "error",
                });
              } else if (reason.response!.status === 422) {
                setHelperText("Invalid SteamID or URL");
              }
              console.log(reason);
            });
        }}
      >
        Add Ban
      </Button>
			<Modal show={showSearch} onHide={handleCloseSearch}>
				<Modal.Header closeButton>
          <Modal.Title>Searching for {playerName} on our servers.</Modal.Title>
        </Modal.Header>
        <Modal.Body>
					{!searchEnd && 
					<>
						<LinearProgress />
						<p>Searching on our servers...</p>
					</>
					}
					{searchEnd && found &&
					<p>
						Found player on {serverName} and kicked them.
					</p>}
					{searchEnd && !found &&
					<p>
						Player wasn't found, but the ban was successfuly added.
					</p>}
        </Modal.Body>
			</Modal>
    </>
  );
}

render(<App />, document.getElementById("app"));
