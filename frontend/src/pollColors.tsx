import React, { CSSProperties, useState } from "react";
import { render } from "react-dom";

import { ColorShow } from "./pollColors/colorShow";
import { Pickers } from "./pollColors/pickers";

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

render(<App />, document.getElementById("app"));
