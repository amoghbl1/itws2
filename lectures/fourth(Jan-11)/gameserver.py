
#import SimpleHTTPServer
import BaseHTTPServer
import SocketServer

httpd = None
keep_running = True

class GameServer(BaseHTTPServer.BaseHTTPRequestHandler):
    TCP_PORT = 54321

    def do_GET(self):
        print "path: ", self.path

        self.serveRequest()

    def serveRequest(self):
    	resource = self.path.lower()
        response = 200
    	if resource == "/": 
	        body = "<html><head></head><body>Empty Reesponse</body></html>"
        elif resource == "/weapon/arrow" or resource ==  "/weapon/arrow/":
        	body = "<html><head></head><body>{weapon: 'arrow', type: 'lethal', range: '10'}</body></html>"
        elif resource == "/stop" or resource ==  "/stop/":
            print "will stop next!!"
            global keep_running
            keep_running = False

            body=""
        else:
            body = "<html><head></head><body><h1>Unknown Request!</h1></body></html>"
            response = 400

        self.send_response(response)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", len(body))
        self.end_headers()
        self.wfile.write(body)


SocketServer.TCPServer.allow_reuse_address = True
httpd = SocketServer.TCPServer(("127.0.0.1", GameServer.TCP_PORT), GameServer)
#httpd = SocketServer.TCPServer(("192.168.2.13", GameServer.TCP_PORT), GameServer)
keep_running = True

print "serving at port", GameServer.TCP_PORT
while keep_running:
    httpd.handle_request()

exit(0)








