const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema, graphql } = require('graphql');

//DB처럼 한 줄에 schema 만들기. input 형식은 입력받기 위한겨~. 수정 삭제 등록은 mutation으로 처리할겨
const schema = buildSchema(`   

    input ProductInput {
        name : String
        price : Int
        description : String
    }

    type Product {
        id : ID!
        name : String
        price : Int
        description : String
    }

    type Query{
        getProduct(id : ID!) : Product
    }

    type Mutation {
        addProduct( input : ProductInput ) : Product
    }
`); //type Mutation. 입력받은 데이터를 Product로 return

const products = [{ //임시 데이터 만들어줌
    id : 1,
    name : '첫번째 제품',
    price : 2000,
    description : '희희'
}, {
    id : 2,
    name : '두 번째 제품',
    price : 4000,
    description : '와하학'
}]

//입력 방식 : { getProduct(id : 1) { name \n price } }
const root = {
    getProduct : ({ id }) => products.find(product => product.id === parseInt(id)),    //내가 입력한 product id랑 일치하는 id의 제품을 한 줄 가져올거임
    addProduct: ({input}) => {
        input.id = parseInt(products.length + 1);
        products.push(input);   //넣어주는 data push
        return root.getProduct({id : input.id});
    },
};

const app = express();
app.use('/graphql', graphqlHTTP({   //url graphql로 통일
    schema : schema,
    rootValue : root,
    graphiql : true //GUI 제공함으로써 query 사용 가능하게 함   와우 신기한 창이 뜨네
}));

app.listen(4000, ()=>{  //여기서 4000은 portnum
    console.log('running server port 4000');
});
// localhost:4000/graphql 해서 나오는 화면에서 url로 호출하면 응답해주는 graphql 서버 만들어줌
// 새로 깔은 postman 프로그램에서 get 자리에 http://localhost:4000/graphql?query={nodejs} 입력해주면 사전에 넣어놨던 값 20이 나옴