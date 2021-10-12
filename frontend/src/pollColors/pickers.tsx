import React, { CSSProperties } from "react";

import { circleContainer } from "./styles";
import { CirclePicker } from "./circlePicker";

export function Pickers(props): JSX.Element {
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
