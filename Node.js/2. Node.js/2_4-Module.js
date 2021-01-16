// module 내보낼 땐 Module.exports
// 불러올 땐 require 파일명

//변수 내보내기
module.exports.a = "Hello a";

//함수 내보내기
function Myfunc(){
    this.name = "my instance";
    this.hello = "my instance hello";
}
module.exports = Myfunc;
