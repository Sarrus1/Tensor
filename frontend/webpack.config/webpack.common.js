var path = require('path');
module.exports = {
  entry: {
    bans_list: path.join(__dirname, "../src/bans-list.tsx"),
    ban_add: path.join(__dirname, "../src/ban-add.tsx"),
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