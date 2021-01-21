const { Router } = require('express');
const router = Router();
const ctrl = require('./admin.ctrl');

router.get('/products', ctrl.get_products );

router.get('/products/write', ctrl.get_products_write );

router.post('/products/write', ctrl.post_products_write );

router.get('/products/detail/:id', ctrl.get_products_detail );

router.get('/products/edit/:id', ctrl.get_products_edit);   //form 채우기. url요청, post요청

router.post('/products/edit/:id', ctrl.post_products_edit); //update. action으로 method만 바뀜

router.get('/products/delete/:id', ctrl.get_products_delete);

module.exports = router;


