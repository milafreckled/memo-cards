from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import base64

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
class Server(BaseHTTPRequestHandler):
   
    def parse_request(self):
            if not BaseHTTPRequestHandler.parse_request(self):
                return False
    
            logging.debug("parsed request <%s> <%s> <%s>" % (self.command, self.path, self.request_version))   
            return True
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", 'text/html')
        self.end_headers()    
    def do_GET(self):
        if self.connection:
            
            
            """
            if self.path=="/":
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                print("Request line"+self.requestline)
                self.wfile.write(self.path.encode("utf-8"))
                self.wfile.write('<h1 style="text-align: center">Choose the operation:</h1>'.encode("utf-8"))
                self.wfile.write('<a href="/good"><button type="button" style="text-align: center">Good</button></a>'.encode("utf-8"))
                self.wfile.write('<a href="/bad"><button type="button" style="text-align: center">Bad</button></a>'.encode("utf-8"))
                """
            if self.path.endswith(".png"):
                self.send_response(200)
                self.send_header('Content-Type', 'image/png')
                self.end_headers()
                self.wfile.write(load("good.png"))
          
            elif self.path=="/bad":
                self.send_response(200)
                self.send_header('Content-Type', 'image/jpeg')
                self.end_headers()
                self.wfile.write(load("bad.jpeg"))

            
def load(file):
    with open(file, "rb") as file_to_load:
        return bytes(str(file_to_load.read()), 'UTF-8')
    
         

def run(server_class=HTTPServer, handler_class=Server, port=8081):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Server is running on port %d" % httpd.server_port)
    logging.debug("%s - server address"%str(httpd.server_address))
    httpd.serve_forever()
    
    
    
if __name__ == "__main__":
    run()