import React, { CSSProperties, useState } from "react";
import { render } from "react-dom";

const circleContainer: CSSProperties = {
  display: "flex",
  height: "5rem",
};

function App(props): JSX.Element {
  const [colors, setColors] = useState([]);
  // Force re-render
  const [nb, setNb] = useState(0);

  const addOrRemoveColor = (color: string): void => {
    if (colors.includes(color)) {
      setColors(colors.filter((element) => element != color));
      setNb(nb - 1);
    } else {
      if (colors.length == 0) {
        setColors([color]);
      } else {
        var newColors = colors;
        newColors.push(color);
        setColors(newColors);
      }
      setNb(nb + 1);
    }
  };

  return (
    <>
      <ColorShow key={nb} colors={colors} />
      <br style={{ clear: "both" }}></br>
      <Pickers addOrRemoveColor={addOrRemoveColor} />
    </>
  );
}

function ColorShow(props): JSX.Element {
  const colors: string[] = props.colors;
  console.log(colors);
  if (colors.length == 0) {
    return <Color color={""} number={0} />;
  } else {
    return (
      <>
        {colors.map((e: string, i: number) => (
          <Color key={i} color={e} number={colors.length} />
        ))}
      </>
    );
  }
}

function Color(props): JSX.Element {
  var color: string = props.color == "" ? "white" : props.color;
  var number: number = props.number == 0 ? 1 : props.number;
  const widthRaw: number = 100 / number;
  const width: string = `${Math.floor(widthRaw)}%`;
  return (
    <div
      style={{
        backgroundColor: color,
        height: "90vh",
        width: width,
        float: "left",
      }}
    ></div>
  );
}

function Pickers(props): JSX.Element {
  const addOrRemoveColor = props.addOrRemoveColor;
  return (
    <div style={circleContainer}>
      <CirclePicker
        color={"green"}
        onClick={(e) => addOrRemoveColor("green")}
      />
      <CirclePicker color={"red"} onClick={(e) => addOrRemoveColor("red")} />
      <CirclePicker
        color={"yellow"}
        onClick={(e) => addOrRemoveColor("yellow")}
      />
      <CirclePicker color={"blue"} onClick={(e) => addOrRemoveColor("blue")} />
    </div>
  );
}

function CirclePicker(props): JSX.Element {
  const circleStyle: CSSProperties = {
    width: "100%",
    height: "auto",
    border: "1px solid black",
    borderRadius: "50%",
    float: "left",
    backgroundColor: props.color,
  };

  return <div onClick={props.onClick} style={circleStyle}></div>;
}

render(<App />, document.getElementById("app"));
