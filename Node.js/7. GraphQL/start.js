const {graphql, buildSchema} = require('graphql');

//query 만들고 응답할 data type 지정
const schema = buildSchema(`
  type Query{
    hello : String,
    nodejs : Int
  }
`);

const root = {
  hello : () => 'hello world', //hello라는 query를 hello world로 응답하게 함
  nodejs : () => 20
}

graphql(schema, '{nodejs}' , root).then((response)=> {
  console.log(response);  //response를 화면에 뿌리겠음~
})