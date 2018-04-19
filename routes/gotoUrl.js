//board routes
var express = require('express');
var router = express.Router();

router.get('/', (req, res) => {
    res.render('tmpTest.pug');
});

module.exports = router;
