
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

#Create custom HTTPRequestHandler class
class KodeFunHTTPRequestHandler(BaseHTTPRequestHandler):
    
    #handle GET command
    def do_GET(self):
        rootdir = 'C:/Users/avagrawa/Desktop/IS/jasmine' #file location
        try:

            if self.path == '/':
                path = "/SpecRunner.html"
            else:
                path = self.path    

            fileName, fileExtension = os.path.splitext(self.path)
            a = self.getHeader(fileExtension)
            if a:
                header = a
            else:
                header = 'text-html'    
            print fileName+fileExtension    
            f = open(rootdir + path) #open requested file

            #send code 200 response
            self.send_response(200)

            #send header first
            self.send_header('Content-type',header)
            self.end_headers()

            #send file content to client
            self.wfile.write(f.read())
            f.close()
            return
            
        except IOError:
            self.send_error(404, 'file not found')



    def getHeader(self,requesttype):
        if requesttype == ".html":
            return 'text-html'
        elif requesttype == ".js":
            return 'application/javascript'
        elif requesttype == ".css":
            return 'text/css'
        else:
            return 'text-plain'           

    
def run():
    print('http server is starting...')

    #ip and port of servr
    #by default http server port is 8081
    server_address = ('localhost', 9999)
    httpd = HTTPServer(server_address, KodeFunHTTPRequestHandler)
    print('http server is running...')
    httpd.serve_forever()
    
if __name__ == '__main__':
    run()