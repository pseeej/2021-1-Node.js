const { Router } = require('express');
const router = Router()

router.use('/', require('./home'));

module.exports = router;