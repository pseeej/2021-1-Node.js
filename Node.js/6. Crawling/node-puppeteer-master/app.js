const express = require('express');
const nunjucks = require('nunjucks');
const logger = require('morgan');
const bodyParser = require('body-parser');

// db 관련
const db = require('./models');

class App {

    constructor () {
        this.app = express();
        
        // db 접속
        this.dbConnection();

        // 뷰엔진 셋팅
        this.setViewEngine();

        // 미들웨어 셋팅
        this.setMiddleWare();

        // 라우팅
        this.getRouting();


    }

    dbConnection(){
        // DB authentication
        db.sequelize.authenticate()
        .then(() => {
            console.log('Connection has been established successfully.');
             return db.sequelize.sync();
            // return db.sequelize.drop();
        })
        .then(() => {
            console.log('DB Sync complete.');
            // 더미 데이터가 필요하면 아래 설정
            //  require('./config/insertDummyData')();
        })
        .catch(err => {
            console.error('Unable to connect to the database:', err);
        });
    }


    setMiddleWare (){
        
        this.app.use(logger('dev'));
        this.app.use(bodyParser.json());
        this.app.use(bodyParser.urlencoded({ extended: false }));
 
    }

    setViewEngine (){

        nunjucks.configure('template', {
            autoescape: true,
            express: this.app
        });

    }

    getRouting (){
        this.app.use(require('./controllers'))
    }

}

module.exports = new App().app;