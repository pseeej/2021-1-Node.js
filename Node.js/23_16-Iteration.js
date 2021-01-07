// for of
//iterable한 객체에 모두 사용 가능. 배열 가능

for (const i of [1, 2, 3]){
    console.log(i);
}

// for in
//모든 property에서 사용 가능

Object.prototype.test = function() {};

for(const i in {a:1, b:2, c:3}){
    console.log(i); //a b c test. prototype의 property인 test까지 같이 출력됨
}