var path = require('path');
var webpack = require('webpack');
const { merge } = require("webpack-merge");
const common = require("./webpack.common.js");
var BundleTracker = require('webpack-bundle-tracker');
module.exports = merge(common, {
	name:'development',
	mode: 'development',
	watch: true,
	devtool : 'inline-source-map',
	plugins: [
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json'
    }),
  ],
});