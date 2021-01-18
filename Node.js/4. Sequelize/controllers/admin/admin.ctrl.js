const models = require('../../models');

exports.get_products = ( _ , res) => {
    // res.render( 'admin/products.html' , 
    //     { message : "hello" } // message 란 변수를 템플릿으로 내보낸다.
    // );

    models.Products.findAll({   //전체 조회하기

    }).then( (products) => {
        res.render('admin/products.html' , { products : products })  //template로 보내기. products:products같이 key값이랑 value값 일치하면 하나만 써도 됨
        // nunjucks에서 반복문 뿌리기 위해 products.html로 이동해서 {% for product in productList %} ~ {% endfor %} 입력해줌
    });
}

exports.get_products_write = ( _ , res) => {
    res.render( 'admin/write.html');
}

exports.post_products_write = ( req , res ) => {
    //res.send(req.body);
    models.Products.create( req.body    //req.body로 아래에 변수 하나씩 지정한 거 한 번에 처리 가능
        //{    //입력된 값들 변수에 저장
        // name : req.body.name,
        // price : req.body.price,
        // description : req.body.description
        //}
    ).then(()=>{
        res.redirect('/admin/products');    //다 하고 나서 main page로 이동해서 list를 보고 싶다. redirect 사용.
    });
}   //다 하고 workbench 들어가서 products 확인하면 입력된 거 들어가있음