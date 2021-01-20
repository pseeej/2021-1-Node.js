const moment = require('moment');

module.exports = (sequelize, DataTypes) => {
    const Products = sequelize.define('Products',
        {
            //id 찾을 땐 findByPk. 한 개만 가져올 땐 findOne으로 조회조건 설정 후 가져오기
            id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true }, //제품 id
            name : { type: DataTypes.STRING },  //제품 이름
            price : { type: DataTypes.INTEGER },    //제품 가격
            description : { type: DataTypes.TEXT }  //제품 설명
        }
    );

    Products.prototype.dateFormat = (date) => (
        moment(date).format('YYYY-MM-DD')
    );

    return Products;
} 