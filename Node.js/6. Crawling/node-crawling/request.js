const request = require('request');

// 네이버 주소 가져오기
const url = "https://www.naver.com";

request(url, (error, response, body) => {  
    console.log(body);
}); //request로 해당 url의 요소들 다 html로 가져옴
    