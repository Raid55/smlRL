let Sequelize = require('sequelize')
let sequelize = new Sequelize('sqlite:./smlRL.db')


module.exports = {
    Sequelize: Sequelize,
    sequelize: sequelize,
    Url: sequelize.import(__dirname + '/url.js') 
}
