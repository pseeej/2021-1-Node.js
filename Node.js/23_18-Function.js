// function
// 이름이 hello인 함수를 선언

function hello1(){  //const hello1 = function(){} 동일
    console.log('hello1');
}
console.log(hello1, typeof hello1);

// 함수의 매개변수
// 함수를 호출할 때 값을 지정

function hello2(name){  //const hello2 = function(){}
    console.log('hello2', name);
}

// 함수의 리턴
// 함수를 실행하면 얻어지는 값

function hello3(name){  //const hello3 = function(){}
    return `hello3 ${name}`;
}
console.log(hello3('Mark'));

// 선언적 function과 익명 함수를 만들어 변수에 할당하는 방법의 차이점
hello4();   //hoisting 수행됨
hello5();   //hoisting 수행 X. var) not a function
hello6();   //hoisting 수행 X. const) undefined

function hello4(){
    console.log('hello4');
}

var hello5 = function(){
    console.log('hello5');
}

const hello6 = function(){
    console.log('hello6');
}

// 생성자 함수로 함수 만들기
// new Function(인자 1, 인자 2, ..., 함수의 바디);

const sum = new Function('a', 'b', 'c', 'return a+b+c'); 
console.log(sum);

// function과 new Function()의 차이

globalThis.a = 0;

{
    const a = 1;
    const test = new Function('return a');
    console.log(test());    //const a is not defined. global.a를 인식함
}

{
    const a =2;
    const test = function() {
        return a;
    };
    console.log(test());    //const a의 값이 출력됨
}

// arrow 함수를 이름이 hi인 변수에 할당
const hi1 = () =>{
    console.log('hi1');
};

// 함수의 매개변수. 함수를 호출할 때 값을 지정
const hi2 = name => {
    console.log('hi2', name);
};

const hi3 = (name, age) =>{
    console.log('hi3', name, age);
};

// 함수의 리턴. 함수를 실행하면 얻어지는 값
const hi4 = name => {
    return `hi4 ${name}`;
};

const hi5 = name => `hi5${name}`;

//생성자 함수를 이용하여 새로운 객체를 만들어 내는 방법
function Person(name, age){
    console.log(this);
    this.name = name;
    this.age = age;
}

const p = new Person('Mark', 37);
console.log(p, p.name, p.age);

const a = new Person('Anna', 26);
console.log(a, a.name, a.age);

const Cat = (name, age)=>{  //not a constructor
    this.name = name;
    this.age = age;
}
// const c = new Cat('냥이', 1); 불가. arrow function 내에서는 this가 생기지 않기 때문.


// 함수를 호출하면 함수를 만들어서 리턴
function plus(base){
    return function(num){
        return base + num;
    }
}

const plus5 = plus(5);  //base의 값이 5
plus5(10);  //num의 값이 10이 됨
console.log(plus5(10)); //15출력

// 함수를 인자로 하여 함수를 호출
function haha(c){
    console.log('hello');
    c();
}

haha(function(){
    console.log('콜백');
})  //hello오ㅏ 콜백 출력됨