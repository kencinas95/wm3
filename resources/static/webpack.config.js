const path = require('path');
const CopyWebpackPlugin = require('copy-webpack-plugin');



module.exports = {
  entry: {
    'jquery/jquery.js': ['jquery'],
    'popper/popper.js': ['@popperjs/core/dist/umd/popper'],
    'bootstrap/bootstrap.js': ['bootstrap/dist/js/bootstrap']
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
            from: path.resolve(__dirname, "node_modules/bootstrap/dist/css/bootstrap.min.css"), to: "bootstrap/bootstrap.min.css"
          },
          {
            from: path.resolve(__dirname, "node_modules/open-iconic"), to: "open-iconic"
          }
        ]
      })
  ]
};