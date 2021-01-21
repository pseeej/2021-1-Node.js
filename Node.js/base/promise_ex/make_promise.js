// Promise : 지연 응답을 통해서 동시성을 제어 하기 위함
// Promise 만드는 규칙
// resolve와 reject를 인자로 가지는 함수 만들기
// 내가 원하는 시점을 resolve로 받아오기
// reject는 내가 error 처리하는 거
// ex) 인증 성공하면 resolve, 실패하면 reject

const wait1second = new Promise((resolve, reject) => {
    
    reject('에러');

});

wait1second.then((result)=> {
    console.log("프라미스 이행 완료");
}).catch((err)=> {  //catch로 reject 받아올 수 있음.
    console.log(err);
});

//시작 -> 1초 뒤에 찍습니다 -> 프라미스 시행 완료