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
    // alert 및 confirm yes 클릭
    page.on("dialog", (dialog) => {
        dialog.accept();
    });  

    // 웹사이트 로딩
    await page.goto('http://localhost:3000/', {timeout: 0, waitUntil: 'domcontentloaded'});

    await page.waitForSelector('.btn-default')
    await page.click('.btn-default');

    // 작성하기 클릭
    await page.waitForSelector('.btn-primary')

    // 폼에 데이터 삽입
    await page.evaluate((a,b) => {
        document.querySelector('input[name=name]').value = a;
        document.querySelector('textarea[name=description]').value = b;
        document.querySelector('.btn-primary').click();
    }, insert_name, insert_description);

    // 첫번째 상세페이지 클릭
    await page.waitForSelector('.btn-default');

    // 각 데이터를 가져오고 싶으면 아래 주석을 해제후 확인해보세요.
    // const tdName = await page.$eval('table tr:nth-child(2) td:nth-child(1) a', td => td.textContent.trim() );
    // const tdDescription = await page.$eval('table tr:nth-child(2) td:nth-child(2)', td => td.textContent.trim() );
    // console.log(tdName);

    await page.click('table tr:nth-child(2) td:nth-child(1) a');

    // 수정하기 클릭
    await page.waitForSelector('.btn-primary');
    await page.click('.btn-primary');
    await page.waitForSelector('.btn-primary');

    // 글수정하기
    await page.waitForSelector('.btn-primary');
    await page.evaluate((a,b) => {
        document.querySelector('input[name=name]').value = a;
        document.querySelector('textarea[name=description]').value = b;
        document.querySelector('.btn-primary').click();
    }, modi_name, modi_description);

    // 글 목록보기
    await page.waitForSelector('.btn-default');
    await page.click('.btn-default');
    await page.waitForSelector('.btn-default');

    // 삭제하기 클릭
    await page.click('.btn-danger');

    // 브라우저 닫기
    await browser.close();
}

run();
