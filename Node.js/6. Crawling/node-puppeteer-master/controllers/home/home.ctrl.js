const models = require('../../models');

exports.index = async ( _ ,res) => {

    try{

        const products = await models.Products.findAll();

        res.render( 'products.html' , { products });

    }catch(e){
        console.log(e);
    }

}

exports.get_write = ( _ , res ) => {
    res.render( 'edit.html' );
}

exports.post_write = async (req,res) => {

    try{
        await models.Products.create(req.body);
        res.redirect('/');
    }catch(e){
        console.log(e);
    }
};

exports.get_detail = async( req , res ) => {
    const product = await models.Products.findByPk(req.params.id);
    res.render( 'detail.html' ,{ product });
}

exports.get_edit = async ( req , res ) => {
    const product = await models.Products.findByPk(req.params.id);
    res.render( 'edit.html' , { product });
}

exports.post_edit = async ( req , res ) => {
    await models.Products.update(
        req.body , 
        { 
            where : { id: req.params.id } 
        }
    );
    res.redirect('/detail/' + req.params.id );
}

exports.get_delete = async( req , res ) => {
    await models.Products.destroy({
        where: {
            id: req.params.id
        }
    });
    res.redirect('/');
}
