var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const UglifyJSPlugin = require("uglifyjs-webpack-plugin");
module.exports = {
  name: "production",
  mode: "production",
  watch: false,
  devtool: "inline-source-map",
  entry: {
    sourcebans: path.join(__dirname, "./src/sourcebans.tsx"),
  },
  output: {
    path: path.join(__dirname, "../backend/static/js"),
    filename: "[name].js",
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: "webpack-stats.json",
    }),
    new CleanWebpackPlugin(),
    new webpack.DefinePlugin({
      "process.env.NODE_ENV": JSON.stringify("production"),
    }),
    new UglifyJSPlugin(),
  ],
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
};
