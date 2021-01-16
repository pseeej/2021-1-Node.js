const express = require('express');
const nunjucks = require('nunjucks');
const logger = require('morgan');
const bodyParser = require('body-parser');  //express의 내장 모듈이기 때문에

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
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended : false}));

app.use('/uploads', express.static('uploads'));  //정적 폴더 셋팅. app.use(url, 폴더명);

app.use((req, res, next) => {
    app.locals.isLogin = true;  //isLogin이라는 global variable 정의하고 값 true로 선언. 이 isLogin 변수는 어디서든 사용 가능
    app.locals.req_path = req.path; //현재 url 보내주는 변수
    next();
});

app.get('/', (req, res) => {
    res.send('express start');
});

function vipMiddleware(req, res, next){ 
    console.log('최우선 미들웨어');
    next(); //꼭 해주세용
}

app.use('/admin', admin);    //여기에 들어가는 미들웨어가 가장 최우선? 미들웨어임
app.use('/contacts', contacts);

//error handling
app.use((req, res, _) => {  //사용하지 않는 변수는 _로 표현해도 됨
    res.status(400).render('common/3_10-404.html'); //상태가 400일 때 render(~)로 ~에 있는 파일 보여줘라
});
app.use((req, res, _) => { 
    res.status(500).render('common/3_10-500.html');
});


app.listen(port, ()=>{
    console.log('Express listening on port', port);
});