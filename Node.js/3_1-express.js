/* EXPRESS 사용 없이 띄우기
const http = require('http');   //node js 내장 모듈 불러오기

http.createServer( (request, response) => {  //서버 띄우기. port 번호 3000번으로
    //1xx 조건부 응답 2xx 응답 성공 3xx 리다이렉션 4xx 요청 오류 5xx 서버 오류 // 응답 상태 코드
    response.writeHead(200, {'Content-Type' : 'text/plain'});   //문서 타입 지정
    response.write('Hello Server'); //화면에 나오는 내용
    response.end();
}).listen(3000);
*/

//express 사용
const express = require('express');

const app = express();
const port = 3000;

app.get('/', (req, res) => {    //get요청은 내가 url을 domain 창에 쳤을 때 나오는 것
    res.send('hello express');  //response send
});

app.get('/fastcampus', (req, res) => {  //앞에는 url, 뒤에는 function문
    res.send('fastcampus get');
})

app.listen(port, () =>{
    console.log('Express listening on port', port);
});

//변경사항 반영하려면 매번 실행되던 거 끄고 다시 하고 반복해야되는데 nodemon 이용하면 그냥 저장만 해도 반영됨
//package.json에 npm start랑 npm run dev 설정해뒀음.