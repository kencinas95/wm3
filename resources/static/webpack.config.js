const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');

module.exports = {
  entry: {
    "index.js": ['./index.js']
  },
  resolve: {
    extensions: ['.js']
  },
  output: {
    path: path.resolve(__dirname, 'lib'),
    filename: "[name]"
  },
  plugins: [
      new CopyWebpackPlugin({
        patterns: [
          {
            from: path.resolve(__dirname, "node_modules/jquery/dist/jquery.min.js"),
            to: "jquery/jquery.js"
          },
          {
            from: path.resolve(__dirname, "node_modules/@popperjs/core/dist/umd/popper.js"),
            to: "popper/popper.js"
          },
          {
            from: path.resolve(__dirname, "node_modules/bootstrap/dist/js/bootstrap.min.js"),
            to: "bootstrap/bootstrap.js"
          },
          {
            from: path.resolve(__dirname, "node_modules/bootstrap/dist/css/bootstrap.min.css"),
            to: "bootstrap/bootstrap.min.css"
          },
          {
            from: path.resolve(__dirname, "node_modules/open-iconic"),
            to: "open-iconic"
          }
        ]
      })
  ]
};