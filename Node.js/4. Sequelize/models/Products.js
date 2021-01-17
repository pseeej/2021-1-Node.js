module.exports = (sequelize, DataTypes) => {
    const Products = sequelize.define('Products',
        {
            id: { type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true }, //제품 id
            name : { type: DataTypes.STRING },  //제품 이름
            price : { type: DataTypes.INTEGER },    //제품 가격
            description : { type: DataTypes.TEXT }  //제품 설명
        }
    );
    return Products;
} 