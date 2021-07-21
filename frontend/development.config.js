var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
module.exports = {
	name:'development',
	mode: 'development',
	watch: true,
	devtool : 'inline-source-map',
	entry: {
		sourcebans: path.join(__dirname, './src/sourcebans.tsx'),
	},
	output: {
    path: path.join(__dirname, '../backend/static/js'),
    filename: '[name].js'
  },  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json'
    }),
  ],
	module: {
		rules: [
			{
				test: [/\.jsx?$/, /\.tsx?$/],
        use: 'babel-loader',
        exclude: /node_modules/,
			}
		]
	}
}