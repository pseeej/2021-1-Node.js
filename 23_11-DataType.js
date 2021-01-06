// Boolean

/*
const isTrue = true;
const isFalse = false;

console.log(isTrue, typeof isTrue);
console.log(isFalse, typeof isFalse); 

const a = new Boolean(false);

console.log(a, typeof a);   //object type

if(a){
    console.log('false?');
}   //a 자체가 새로운 객체로써의 값을 갖고 있기 때문에 출력됨

const b = Boolean(false);

console.log(b, typeof b);

if(b){
    console.log('false?');
}   //출력 안 됨
*/


// Null

/*
const a = null;

console.log(a, typeof a);   //object type. 비어 있는 값 의미하는 undefined

// Undefined

let b;
console.log(b, typeof b);   //undefined type. 아무 값도 할당하지 않았을 때

if(a==b){
    console.log(a==b);  //true 출력됨
}

if(a===b){
    console.log(a===b); //false
}
*/

// Number

/*
const a = 37;
console.log(a, typeof a); //number

const b = 96.7;
console.log(b, typeof b); //number

const c = NaN;
console.log(c, typeof c); //number. Not a Number

const d = Number('Mark');
console.log(d, typeof d); //NaN. 문자형->숫자형 형 변환 불가

const e = Number('37');
console.log(e, typeof e); //Number
*/

// String

/*
const a = 'Mark';
console.log(a, typeof a);   //string

const b = "Mark" + "Lee";

const c = a + "Lee";
console.log(c, typeof c); //MarkLee String

const d = `${a} Lee`;   //Template string. `로 감싼 내용 그대로 출력 가능
console.log(d, typeof d);  //Mark Lee String
*/

// Symbol

const a = Symbol();
const b = Symbol(37);
const c = Symbol('Mark');
const d = Symbol('Mark');

console.log(a, typeof a);
console.log(c===d); //Symbol에 같은 값을 넣어줘도 각자 고유한 symbol이 됨

//new Symbol();   //New로 만드는 게 아님~
