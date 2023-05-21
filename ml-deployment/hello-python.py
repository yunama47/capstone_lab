#/usr/bin/env python3

import http
import http.server
import socket
import socketserver
import sys

# TCP port for listening to connections, if no port is received
DEFAULT_PORT=8080

with open('http-server/hello-world.html', 'rb') as html:
    html_content = html.read()

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(http.HTTPStatus.OK)
        self.end_headers()
        # Html
        self.wfile.write(html_content)

def main(argv):
    port = DEFAULT_PORT
    if len(argv) > 1:
        port = int(argv[1])

    web_server = socketserver.TCPServer(('', port), Handler)
    print("Listening for connections on port {}".format(port))
    web_server.serve_forever()


if __name__ == "__main__":
    main(sys.argv)