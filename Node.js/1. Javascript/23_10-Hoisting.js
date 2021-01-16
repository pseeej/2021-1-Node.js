//아래에 있는 함수와 변수의 "선언부"만을 끌어올리는 것이 Hoisting

// // 함수 먼저 호출 나중에
// function hello1(){
//     console.log('hello1');
// }

// hello1();

// // 호출 먼저 함수 나중에
// hello2();

// function hello2(){
//     console.log('hello2');
// }

console.log(name);  //Woongjae가 아닌 undefined 출력됨

name = 'Mark';

console.log(name);  //Mark 출력됨

var name = "Woongjae";
//var는 hoisting 일어나지만 let은 hoisting 현상 일어나지 않음.