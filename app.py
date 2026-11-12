
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 8080))

class ShipItHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>ShipIt App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 100px 20px;
                    background: #f4f7fb;
                }
                h1 { color: #2563eb; }
            </style>
        </head>
        <body>
            <h1>Welcome to ShipIt!</h1>
            <p>Your application is running successfully.</p>
            <p>Deployed with Docker and Azure Container Apps.</p>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", PORT), ShipItHandler)
print(f"ShipIt running on port {PORT}", flush=True)
server.serve_forever()
