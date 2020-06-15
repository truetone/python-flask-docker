const path = require('path');

module.exports = {
  entry: { index: path.resolve(__dirname, "truetone", "static", "js", "src", "index.js") },

  output: {
    filename: 'index.js',
    path: path.resolve(__dirname, "truetone", "static", "js", 'dist'),
  },

  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        }
      }
    ]
  },
};
