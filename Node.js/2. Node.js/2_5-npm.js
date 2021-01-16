// npm install uuid4

//남이 만든 내장 module에서 찾는 거라 경로 없어도 됨
const uuid4 = require('uuid4');
console.log(uuid4());

//express = ladash v3에서 최적화되어있음
//uuid4 = lodash v4에서 최적화되어있음

//각각의 framework별로 참고하는 module들이 있음
// express는 body-parser라던가,,,

//package-lock.json은 모듈 충돌 방지 위함

//package.json에서의 script
//"scripts": {
//    "start": "node index.js",
//}라고 적혀있다면 콘솔창에 npm start만 입력해도 바로 node index.js 입력한 것과 같은 결과를 갖게 됨.