//대분류 url + 폴더 위치

const { Router } = require('express');
const router = Router()

router.use('/admin', require('./admin'));   //폴더 지정
//router.use('/contacts', require('./admin'));    //contacts라는 폴더 추가

module.exports = router;