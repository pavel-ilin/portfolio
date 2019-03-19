import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as http:
    print("serving at port", PORT)
    http.serve_forever()
