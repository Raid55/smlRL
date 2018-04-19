const path = require('path');
const express = require('express');
const morgan = require('morgan');
const favicon = require('serve-favicon');
const bodyParser = require('body-parser');

//Importing routes
const { home } = require('./routes');

//express app
const app = express();


// Serve static assets
app.use('/files',express.static('public'));
// Serving favicon
app.use(favicon(__dirname + '/public/favicon-16x16.png'));

//body parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

// View engine
app.set('view engine', 'pug');

//Morgan logger//
app.use(morgan("........................................"));
app.use(morgan(':user-agent'));
app.use(morgan('[:date[clf]]'));
app.use(morgan('":method | :url | HTTP/:http-version"'));
app.use(morgan(':status | :res[content-length] | :response-time ms'));
app.use(morgan('........................................'));
app.use(morgan(' '));
//end of logger info//

//Applying Routes
app.use('/', home);


module.exports = app;
