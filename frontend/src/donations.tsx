import React, { useState, useEffect } from "react";
import { render } from "react-dom";
import { emphasize, TextField } from "@material-ui/core";
import { Modal, Button } from "react-bootstrap";
import axios from "axios";
import { PayPalButton } from "react-paypal-button-v2";
var dayjs = require("dayjs");

const dayJSFormat = "D MMMM YYYY";

interface donationDuration {
  length: string;
  end: string;
}

function getDuration(amount): donationDuration {
  if (amount >= 15) {
    return { length: "1 year", end: dayjs().add(1, "y").format(dayJSFormat) };
  }
  if (amount >= 5) {
    return { length: "3 months", end: dayjs().add(3, "M").format(dayJSFormat) };
  }
  if (amount >= 2) {
    return { length: "1 month", end: dayjs().add(1, "M").format(dayJSFormat) };
  }
  if (amount >= 1) {
    return { length: "1 week", end: dayjs().add(1, "w").format(dayJSFormat) };
  }
  return { length: "", end: ""};
}

function getCurrentDate(): string {
  let now = dayjs();
  return now.format(dayJSFormat);
}

function App(props): JSX.Element {
  const [steamID, setSteamID] = useState("");
  const [amount, setAmount] = useState(0);
  const [steamProfile, setSteamProfile] = useState();
  const [personaName, setPersonaName] = useState();

  const [profilePic, setprofilePic] = useState("");

  const [showConfirmation, setshowConfirmation] = useState(false);

  const handleCloseConfirmation = () => setshowConfirmation(false);
  const handleShowConfirmation = () => setshowConfirmation(true);

  const profilePicStyle: React.CSSProperties = {
    borderRadius: "50%",
    textAlign: "center",
  };

  const containerStyle: React.CSSProperties = {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
  };

  const confirmationText: React.CSSProperties = {
    textAlign: "center",
  };

  return (
    <>
      <form
        onSubmit={async (event) => {
          event.preventDefault();
          setSteamID(event.target.steamid.value);
          setAmount(event.target.amount.value);
          await axios
            .get(`/api/steamuserinfo?steamid=${event.target.steamid.value}`)
            .then((res) => {
              setprofilePic(res.data["avatarfull"]);
              setPersonaName(res.data["personaname"]);
              setSteamProfile(res.data["profileurl"]);
              handleShowConfirmation();
            });
        }}
      >
        <TextField
          label="Amount"
          variant="outlined"
          size="small"
          name="amount"
          type="number"
          style={{ marginRight: 8, width: "40%" }}
        />
        {"  "}
        <TextField
          label="Steam"
          style={{ marginLeft: 8, width: "40%" }}
          placeholder="https://steamcommunity.com/id/gabelogannewell"
          variant="outlined"
          size="small"
          name="steamid"
        />
        {"  "}
        <Button
          type="submit"
          name="submit"
          variant="secondary"
          style={{ marginLeft: 8 }}
        >
          Confirm
        </Button>
      </form>
      <Modal show={showConfirmation} onHide={handleCloseConfirmation}>
        <Modal.Header closeButton>
          <Modal.Title>Confirmation</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <div className="row">
            <div className="col-12">
              <h3 style={confirmationText}>Please confirm that this is you:</h3>
            </div>
          </div>
          <div className="row">
            <div className="col-12" style={containerStyle}>
              <img src={profilePic} style={profilePicStyle}></img>
            </div>
          </div>
          <div className="row" style={{ marginTop: "2rem" }}>
            <div className="col-12" style={containerStyle}>
              <a href={steamProfile}>
                <h4>{personaName}</h4>
              </a>
            </div>
          </div>
          <div className="row" style={{ marginTop: "2rem" }}>
            <div className="col-12" style={{ textAlign: "center" }}>
              <h3>Please confirm that the donation amount is correct:</h3>
              <br />
              <h4>
                You wish to donate <b>{amount}€</b>
              </h4>
              <br />
              For your generosity, you will receive the VIP status for{" "}
              <b>{getDuration(amount).length}</b>, starting on <b>{getCurrentDate()}</b> and ending
              on <b>{getDuration(amount).end}</b>.
              <br />
              <br />
              If this is you, and you agree, please click below, to proceed with
              your donation, you will be redirected to PayPal to process your
              contribution.
            </div>
          </div>
          <div className="row" style={{ marginTop: "2rem" }}>
            <div className="col-12" style={{ textAlign: "center" }}>
              <PayPalButton
                createOrder={(data, actions) => {
                  return actions.order.create({
                    intent: "CAPTURE",
                    purchase_units: [
                      {
                        description: "Tensor VIP",
                        amount: {
                          currency_code: "EUR",
                          value: amount,
                        },
                        on0: "SteamID",
                        os0: steamID,
                        on1: "Name",
                        os1: personaName,
                      },
                    ],
                  });
                }}
                shippingPreference="NO_SHIPPING"
                onSuccess={(details, data) => {
                  alert("Your order has been processed.");
                }}
                options={{
                  clientId: clientID,
                }}
              />
            </div>
          </div>
        </Modal.Body>
      </Modal>
    </>
  );
}

render(<App />, document.getElementById("root"));
