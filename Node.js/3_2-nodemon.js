var http= require('http');

http.createServer(function(request, response){
    response.writeHead(200, {'Content-Type' : 'text/plain'});
    response.write('Hello Nodejs3');
    response.end();
}).listen(3000);