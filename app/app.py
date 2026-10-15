from http.server import BaseHTTPRequestHandler, HTTPServer
import os

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        if self.path == "/health":
            self.wfile.write(b"ok")
        else:
            self.wfile.write(f"Hello from version {os.getenv('APP_VERSION', 'dev')}".encode())

HTTPServer(("", 8080), Handler).serve_forever()