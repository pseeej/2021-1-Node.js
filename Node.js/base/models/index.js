var Sequelize = require('sequelize');
var path = require('path');
var fs = require('fs');
var dotenv = require('../../node_modules/dotenv'); //dotenv 가져오기

dotenv.config(); //LOAD CONFIG

const sequelize = new Sequelize( process.env.DATABASE,  //.env에 있는 요소?들 사용 방식
process.env.DB_USER, process.env.DB_PASSWORD,{  //DB 접속
    host: process.env.DB_HOST,
    dialect: 'mysql',
    timezone: '+09:00', //한국 시간 셋팅
    operatorsAliases: Sequelize.Op,
    pool: {
        max: 5,
        min: 0,
        idle: 10000
    }
});

let db = [];

fs.readdirSync(__dirname)    //각각의 파일들 참조하고 sync 걸어서 테이블들 생성함.
    .filter(file => {
        return file.indexOf('.js')&& file !== 'index.js'    //index.js를 제외한 나머지 모든 파일
    })
    .forEach(file => { 
        var model = sequelize.import(path.join(__dirname,
            file));
            db[model.name] = model;
    });

Object.keys(db).forEach(modelName => {  //외부 키 들어올 때 setting
    if("associate" in db[modelName]){   //하위 테이블들에서는 foreign key,,,  암튼 model간의 관계
        db[modelName].associate(db);
    }
});

db.sequelize = sequelize;
db.Sequelize = Sequelize;

module.exports = db; 