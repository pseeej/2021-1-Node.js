const models = require('./models');

async function getProducts() {
    /* models.Products.findByPk(req.params.id).then((product)=>{   //primary key로 찾은 다음에
        res.render('admin/detail.html', {product : product});  //rendering 시도
    }); */ //이 코드를 아래처럼 쓰는겨 then 대신에 await 사용

    //error 처리
    try {
        //await으로 promise 객체 받을 수 있음
        const product2 = await models.Products.findByPk(2);
        const product7 = await models.Products.findByPk(7);

        console.log(product2.dataValues); //dataValues로 모든 data 가져옴. {product : product}와 같은 의미라고 생각하면 됨
        console.log(product7.dataValues);

    } catch (err) {
        console.log(err);
    }

}

getProducts();