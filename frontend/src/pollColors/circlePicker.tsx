import React, { CSSProperties } from "react";

export function CirclePicker(props): JSX.Element {
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
