var path = require('path');
module.exports = {
  entry: {
    sourcebans: path.join(__dirname, "../src/sourcebans.tsx"),
    donations: path.join(__dirname, "../src/donations.tsx"),
    servers: path.join(__dirname, "../src/servers.tsx"),
  },
  output: {
    path: path.join(__dirname, "../../backend/static/js"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: [/\.jsx?$/, /\.tsx?$/],
        use: {
          loader: "babel-loader",
          options: {
            presets: [['@babel/preset-env', { modules: false }], "@babel/react"],
          },
        },
        exclude: /node_modules/,
      },
    ],
  },
}