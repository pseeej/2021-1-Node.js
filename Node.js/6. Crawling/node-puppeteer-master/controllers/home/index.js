const { Router } = require('express');
const router = Router();
const ctrl = require('./home.ctrl');

router.get('/', ctrl.index);
router.get('/write', ctrl.get_write);
router.post('/write', ctrl.post_write);
router.get('/detail/:id', ctrl.get_detail);
router.get('/edit/:id', ctrl.get_edit);
router.post('/edit/:id', ctrl.post_edit);
router.get('/delete/:id', ctrl.get_delete);

module.exports = router;
