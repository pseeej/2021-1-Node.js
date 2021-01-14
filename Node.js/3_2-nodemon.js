var http= require('http');

http.createServer(function(request, response){
    response.writeHead(200, {'Content-Type' : 'text/plain'});
    response.write('Hello Nodejs');
    response.end();
}).listen(3000);

//nodemon 설치 안 해도 되게 하려면 npx 이용
//npx nodemon ~~하면 됨