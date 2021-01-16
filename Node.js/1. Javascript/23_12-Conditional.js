// False

if (false);
if (0);
if ('');
if (null);
if (NaN);

// False만 아니면 나머지 다 True. 그냥 값 있으면 다 True


// 조건 ? 조건이 참이면 실행되는 표현식 : 조건이 거짓이면 실행되는 표현식
 
let n = 7;
console.log(n%5===0 ? '5의 배수입니다.' : '5의 배수가 아닙니다.');

let m=5;
const msg = m%5===0 ? '5의 배수입니다.' : '5의 배수가 아닙니다.';
console.log(msg);