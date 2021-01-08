const myvar = require('./2_4-Module');
console.log(myvar.a);

//함수 불러오기
const myfunc = require('./2_4-Module');
const setFunc = new myfunc();
console.log(setFunc.name);