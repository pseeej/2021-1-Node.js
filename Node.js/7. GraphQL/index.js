const express = require('express');
const { graphqlHTTP } = require('express-graphql');
const { buildSchema, graphql } = require('graphql');

const schema = buildSchema(`
    type Query{
        hello : String,
        nodejs : Int
    }
`);

const root = {
    hello : () => 'hello world',
    nodejs : () => 20
}

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