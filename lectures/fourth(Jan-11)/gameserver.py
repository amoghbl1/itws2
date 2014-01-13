
#import SimpleHTTPServer
import BaseHTTPServer
import SocketServer

class GameServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        print "do get handler!"
        print "path: ", self.path
        print "request: ", self.request
        print "raw_requestline: ", self.raw_requestline
        print "address_string: ", self.address_string
        print "serveRequest: ", self.serveRequest
        print "server: ", self.serveRequest

        self.serveRequest()

    def do_HEAD(self):
        print "do head handler!"
        self.serveRequest()

    def serveRequest(self):
    	resource = self.path.lower()
    	if resource == "/": 
	        body = "<html><head></head><body>Empty Reesponse</body></html>"
        elif resource == "/weapon/arrow":
        	body = "<html><head></head><body>{weapon: 'arrow', type: 'lethal', range: '5'}</body></html>"
        elif 
        else:
        	body = "<html><head></head><body><h1>Unknown Request!</h1></body></html>"
       
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)
        

PORT = 65432

Handler = GameServer

httpd = SocketServer.TCPServer(("127.0.0.1", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
