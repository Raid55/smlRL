const server = require('./app');
let db = require('./models');
const { PORT, ADDRESS } = require('./config');

// db.sequelize.sync({force: true}).then(() => {
db.sequelize.sync().then((test) => {
    console.log(test);
    server.listen(PORT, () => {
        console.log(`Web server starting...`);
        console.log(`App listening at ${ADDRESS}:${PORT}`);
        console.log('...\n');
    });
})
