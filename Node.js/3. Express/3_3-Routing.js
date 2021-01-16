const express = require('express');

const admin = require('./3_3-Routes/3-3_admin');    //해당 주소에 있는 내용 가져오기
const contacts = require('./3_3-Routes/3-3_contacts');

const app = express();
const port = 3000;

app.get('/', (req, res) => {
    res.send('express start');
});

app.use('/admin', admin);   //localhost:3000/admin 이후의 내용을 편리하게 정의 위해...
app.use('/contacts', contacts);

app.listen(port, ()=>{
    console.log('Express listening on port', port);
});