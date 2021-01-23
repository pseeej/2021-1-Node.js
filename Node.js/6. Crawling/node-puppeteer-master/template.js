const puppeteer = require('puppeteer');

//입력 할 텍스트
const insert_name =  "insert_" + Math.random().toString(36).substring(2, 15);
const insert_description = "insert_" + Math.random().toString(36).substring(2, 15);

//수정 할 텍스트
const modi_name = "update_" + Math.random().toString(36).substring(2, 15);
const modi_description = "update_" + Math.random().toString(36).substring(2, 15);

async function run (){

    // 브라우저 열기
    const browser = await puppeteer.launch();
    const page = await browser.newPage();  

    page.on("dialog", (dialog)=> {
        dialog.accept();    //alert창, confirm창같은 거 뜨는 거 그냥 다 yes로 처리함
    });
    

    // 웹사이트 로딩
    await page.goto('http://localhost:3000/', {timeout: 0, waitUntil: 'domcontentloaded'});

    // 상단 테이블의 th 제목을 가져오고 싶은경우
    // const tdName = await page.$eval('table tr:nth-child(1) th:nth-child(1)', th => th.textContent.trim() );
    // console.log(tdName);

    //두 개 다 get 요청으로 나옴
    await page.waitForSelector('.btn-default'); //작성하기까지의 화면이 landing이 되어있어야겠죠,,,? await로 작성하기 버튼까지 기다려줌. btn-default는 작성하기 버튼의 class
    await page.click('.btn-default');   //작성하기로 넘어간 거 확인 가능

    //puppeteer는 다음 화면으로 넘어가기까지의 시점을 잘 정해줘야한다,,,
    await page.waitForSelector('.btn-primary');

    //데이터 넣어줄 거임. 여기 여기 내용 채우고 작성하기를 클릭하라! (이거 하고 나면 post 뜸)
    await page.evaluate((a, b) => {
        document.querySelector('input[name=name]').value = a;   //input[name]에 a를 넣을겨~
        document.querySelector('textarea[name=description]').value = b;
        document.querySelector('.btn-primary').click(); //클릭해주쇼

    }, insert_name, insert_description);    //랜덤으로 생성한 이름과 설명으로 a와 b를 채워줄겨

    //수정하기 해볼겨 (get 다음 detail 화면에서 edit post로 해서 나옴~)
    await page.waitForSelector('.btn-default');
    await page.click('table tr:nth-child(2) td:nth-child(1) a');  //table에서 두 번째 줄에서도 제목 부분이 클릭될 때까지 기다리렴

    //수정하기 누를 때까지 기다려라
    await page.waitForSelector('.btn-primary'); 
    await page.click('.btn-primary');
    await page.waitForSelector('.btn-primary');

    //text ㅊㅐ워넣기
    await page.evaluate((a, b)=> {
        document.querySelector('input[name=name]').value = a;
        document.querySelector('textarea[name=description]').value = b;
        document.querySelector('.btn-primary').click();

    }, modi_name, modi_description);    //수정하기 text랑 description 넣어주기

    //삭제하기
    await page.waitForSelector('.btn-default');
    await page.click('.btn-default');   //목록 보기 클릭해야 돌아가자나
    await page.waitForSelector('.btn-default'); //또 기다리쇼잉~~

    await page.click('.btn-danger');


    // 브라우저 닫기
    await browser.close();
}

run();
