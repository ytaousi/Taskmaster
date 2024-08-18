var http = require('http');

function serve(ip, port)
{
        http.createServer(function (req, res) {
            res.writeHead(200, {'Content-Type': 'text/plain'});
            res.write("\nSome Secrets:");
            res.write("\n"+process.env.SECRET_PASSPHRASE);
            res.write("\n"+process.env.SECRET_TWO);
            res.end("\nThere's no place like "+ip+":"+port+"\n");
        }).listen(port, ip);
        console.log('Server running at http://'+ip+':'+port+'/');
}

// Create a server listening on all networks
serve('0.0.0.0', 9000);