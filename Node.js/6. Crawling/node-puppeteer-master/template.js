const puppeteer = require('puppeteer');

//입력 할 텍스트
const insert_name =  "insert_" + Math.random().toString(36).substring(2, 15);
const insert_description = "insert_" + Math.random().toString(36).substring(2, 15);

//수정 할 텍스트
const modi_name = "update_" + Math.random().toString(36).substring(2, 15);
const modi_description = "update_" + Math.random().toString(36).substring(2, 15);

async function run (){

    // 브라우저 열기
    const browser = await puppeteer.launch({
        //headless : false    //puppeteer는 web browser를 source로 띄움. 이렇게 해두면 web browser 창 뜸
        //headless : true //web browser가 안 뜬다고 생각하면 돼~ 터미널이라고 생각하쇼
    });
    const page = await browser.newPage();  //chromium이라는 browser로 뜸
    

    // 웹사이트 로딩
    await page.goto('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%BD%94%EC%8A%A4%ED%94%BC', {timeout: 0, waitUntil: 'domcontentloaded'});

    //상단 테이블의 th 제목을 가져오고 싶은경우
    const tdName = await page.$eval('.spt_con strong', strong => strong.textContent.trim() );   //네이버에서 코스피 지수 가져오기
    //const tdName = await page.$eval('table tr:nth-child(1) th:nth-child(1)', th => th.textContent.trim() );
    console.log(tdName);

    // 브라우저 닫기
    await browser.close();
}

run();
