const models = require('../../models');

exports.get_products = async (_, res) => {

    //~.then 대신에 promise 객체인 await으로 처리함. 

    //error 처리 위해 try-catch
    try {

        const products = await models.Products.findAll();
        res.render('admin/products.html', {
            products
        }); //template로 보내기. products:products같이 key값이랑 value값 일치하면 하나만 써도 됨

    } catch (e) {

    }


}

exports.get_products_write = (_, res) => {
    res.render('admin/write.html');
}

exports.post_products_write = async (req, res) => {

    await models.Products.create(req.body);
    res.redirect('/admin/products'); //다 하고 나서 main page로 이동해서 list를 보고 싶다. redirect 사용.
}
//다 하고 workbench 들어가서 products 확인하면 입력된 거 들어가있음

exports.get_products_detail = async (req, res) => {
    //req.params.id로 바뀌는 id 받을 수 있음.
    const product = await models.Products.findByPk(req.params.id);
    res.render('admin/detail.html', {product});
}

exports.get_products_edit = async (req, res) => {
    const product = await models.Products.findByPk(req.params.id);
    res.render('admin/write.html', { product });
}

exports.post_products_edit = async (req, res) => {
    //update 조건 두 가지. req body 저장할 데이터, 조건.
    await models.Products.update(
        req.body,
        {
        where: {id: req.params.id} //특정 아이디일 때 저장하기. (조건)
        });
    res.redirect('/admin/products/detail/' + req.params.id); //해당 페이지로 이동
    
}

exports.get_products_delete = async (req, res) => {
    //SQL에서의 DELETE문이랑 동일한 destroy
    await models.Products.destroy({
        where: { //조건 설정
            id: req.params.id
        }
    });
    res.redirect('/admin/products');
    
}