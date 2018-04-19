//board routes
var express = require('express');
let db = require('../models');
var router = express.Router();

router.post('/', (req, res) => {

    db.Url.create({ short_id: '123ertss', full_url: "www.lols.com", time_created: new Date() }).then(task => {
        console.log(task)
    })
    .catch((err) => {
        console.log(err)
    })
});
 
module.exports = router;
