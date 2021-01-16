const express = require('express');
const nunjucks = require('nunjucks');
const logger = require('morgan');

const admin = require('./Routes/3_6-admin');    //해당 주소에 있는 내용 가져오기
const contacts = require('./Routes/3_3-contacts');

const app = express();
const port = 3000;

nunjucks.configure('Template', {
    autoescape : true,  //웬만한 html의 템플릿 보안 향상을 위해. 크로스사이트 공격같은 거,,,?
    express : app
});

//미들웨어 셋팅
//미들웨어는 중간 요청을 가로채는 것
//app.use 자체가 다 미들웨어
app.use(logger('dev')); //GET admin/products 요청했다고 뜸

app.get('/', (req, res) => {
    res.send('express start');
});

function vipMiddleware(req, res, next){ 
    console.log('최우선 미들웨어');
    next(); //꼭 해주세용
}

app.use('/admin', vipMiddleware, admin);    //여기에 들어가는 미들웨어가 가장 최우선? 미들웨어임
app.use('/contacts', contacts);

app.listen(port, ()=>{
    console.log('Express listening on port', port);
});