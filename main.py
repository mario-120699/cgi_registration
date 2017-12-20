import BaseHTTPServer
import CGIHTTPServer

server = BaseHTTPServer.HTTPServer
handler = CGIHTTPServer.CGIHTTPRequestHandler

server_address = ('', 8080)
handler.cgi_directories = ['/cgi']

httpd = server(server_address, handler)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.shutdown()
