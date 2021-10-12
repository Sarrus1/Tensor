import React, { CSSProperties } from "react";

export function ColorShow(props): JSX.Element {
  const colors: string[] = props.colors;

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

export function Color(props): JSX.Element {
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
