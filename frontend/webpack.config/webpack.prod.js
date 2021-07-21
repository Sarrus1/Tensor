var path = require("path");
var webpack = require("webpack");
const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");
var BundleTracker = require("webpack-bundle-tracker");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const UglifyJSPlugin = require("uglifyjs-webpack-plugin");
module.exports = merge(common, {
  name: "production",
  mode: "production",
  watch: false,
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
  ]
});
