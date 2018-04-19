module.exports = function(sequelize, DataTypes) {
    return sequelize.define("Url", {
        id: {
            type: DataTypes.INTEGER,
            allowNull: false,
            autoIncrement: true,
            primaryKey: true,
            unique: true
        },
        short_id: {
            type: DataTypes.STRING(8),
            unique: true,
            allowNull: false
        },
        full_url: {
            type: DataTypes.STRING(2000),
            unique: true,
            allowNull: false
        },
        time_created: {
            type: DataTypes.DATE,
            allowNull: false
        },
        time_accessed: {
            type: DataTypes.DATE,
            allowNull: true
        } 
    });
}
