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

exports.get_products_detail = (req, res) => {
    //req.params.id로 바뀌는 id 받을 수 있음.
    models.Products.findByPk(req.params.id).then((product)=>{   //primary key로 찾은 다음에
        res.render('admin/detail.html', {product : product});  //rendering 시도
    });
};

exports.get_products_edit = (req, res) => {
    models.Products.findByPk(req.params.id).then((product) => { //기존에 있던 내용들로 칸을 채워놔야되니깐.
        res.render('admin/write.html', {product});  //수정하기 창 자체는 작성하기 창이랑 똑같으니깐 write.html 사용해도 됨
    });
}

exports.post_products_edit = (req, res) => {
    //update 조건 두 가지. req body 저장할 데이터, 조건.
    models.Products.update({ 
        // 데이터
        name : req.body.name,
        price : req.body.price,
        description : req.body.description
    },{
        where : {id : req.params.id}    //특정 아이디일 때 저장하기. (조건)
    }
    ).then(()=> {
        res.redirect('/admin/products/detail/' + req.params.id); //해당 페이지로 이동
    })
}