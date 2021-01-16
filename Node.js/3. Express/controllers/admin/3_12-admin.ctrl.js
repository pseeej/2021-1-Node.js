// 실제 라우팅의 컨트롤러 역할

exports.get_products = ( _ , res) => {
    res.render( 'admin/3_5-products.html' , 
        { message : "hello" } // message 란 변수를 템플릿으로 내보낸다.
    );
}

exports.get_products_write = ( _ , res) => {
    res.render( 'admin/3_7-write.html');
}

exports.post_products_write = ( req , res ) => {
    res.send(req.body);
}