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
        updateProduct( id : ID!, input : ProductInput! ) : Product
        deleteProduct( id : ID! ) : String
    }
`); //type Mutation. 입력받은 데이터를 Product로 return. 여기서 어떤 query를 작성하겠다~ 하고 밑에 가서 상세하게 써둠

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
    updateProduct : ({ id, input }) => {    //value에 있는 값과 일치하는 조회 조건을 찾아야함. 필수 요소에 id도 추가됨
        const index = products.findIndex(product => product.id === parseInt(id)) //배열의 indexing 안에 value로 조회해야함.
        products[index] = {
            id : parseInt(id),
            ...input    //안에서 입력했던 값들 객체 그대로 펼쳐진다고 생각하면 됨. operating 연산자
        }
        return products[index];
    },
    deleteProduct : ({id}) => {
        const index = products.findIndex(product => product.id === parseInt(id))
        products.splice(index, 1)    //products에서 slice로 0번부터 1개의 data가 날아간다고 생각하쇼
        return "remove success"
    }
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