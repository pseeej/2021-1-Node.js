const p1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve({ p1_text : "p1의 텍스트"});
    }, 1000)
});

const p2 = new Promise((resolve, reject) => {
    setTimeout(() => {
        //resolve({ p2_text : "p2의 텍스트"});
        reject("error error");
    }, 3000)
});

/* p1.then((result1) => {
    console.log("p1 = " + result1.p1_text);
    return p2;  //return을 promise 객체로 해줬기 때문에
}).then((result2) => {   //그다음에 then이 나올 수 있음
    console.log("p2 = " + result2.p2_text);
}); */

Promise.all([p1, p2]).then((result)=> { //위에 거를 한 번에 작성하는 방법
    console.log("p1 = " + result[0].p1_text);   //result[0] = p1
    console.log("p2 = " + result[1].p2_text);   //result[1] = p2
}).catch(err => {
    console.log(err);
});

//reject 에러처리 하고 싶으면 catch문 쓰면 됨.