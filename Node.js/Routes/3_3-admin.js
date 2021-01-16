const express = require('express');
const router = express.Router();

router.get('/', (req, res)=>{
    res.send('admin 이후 url');
});

router.get('/products', (req, res) =>{
    //res.send('admin products');
    res.render('admin/3_5-products.html', { //response. template에 nunjucks로 뿌려줌
        message : `<h1>메세지가 출력됩니다</h1>`,  //3_4-products.html에 있는 message 내용에 이게 들어감
        online : 'express'  //앞에 있는 online이 3_4-products.html에 있으면 이 내용
    })
});

module.exports = router;