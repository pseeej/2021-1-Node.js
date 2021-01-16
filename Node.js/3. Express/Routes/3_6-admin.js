const express = require('express');
const router = express.Router();

function testMiddleware( req, res, next){   //middleware는 인자를 세 개 가짐. request, response, next
    console.log('첫 번째 미들웨어');
    next(); //다음 단계로 넘어가라
}

function testMiddleware2( req, res, next){
    console.log('두 번째 미들웨어');
    next();
}

/* 실제 이용 예를 들면~
function loginRequired(req, res, next) {
    if(로그인 되어 있지 않으면){
        res.redirect(로그인 창으로);
    }else{
        next();
    }
}
*/

router.get('/', testMiddleware, testMiddleware2, (req, res)=>{   //먼저 주소로 가서, middleware 수행하고, 그다음에 req res 수행하라. 순서대로 진행됨
    res.send('admin 이후 url'); //최종 도달
});

router.get('/products/write', (req, res)=>{
    res.render('admin/3_7-write.html', {islogin : true});   //로그인이 되어있을 때 수행하라
});

router.post('/products/write', (req, res)=>{
    //res.send('1234512');    //작성하기 누르면 이 숫자 뜸
    //res.send(req.body.name);    //3_7-write의 id name
    res.send(req.body); //전체변수
});

// GET /users : 모든 사용자 정보 가져오기
// POST /users : 사용자 추가
// GET /users/(ID) : 한 명만 볼 때
// PUT /users/(ID) : 한 명 수정
// DELETE /users/(ID) : 한 명 삭제

router.get('/products', (req, res) =>{
    //res.send('admin products');
    res.render('admin/3_5-products.html', { //response. template에 nunjucks로 뿌려줌
        message : `<h1>메세지가 출력됩니다</h1>`,  //3_4-products.html에 있는 message 내용에 이게 들어감
        online : 'express'  //앞에 있는 online이 3_4-products.html에 있으면 이 내용
    })
});

module.exports = router;