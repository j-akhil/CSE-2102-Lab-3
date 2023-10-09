#
# PORT 8093
#
#
# PORT 8093
#
#
# PORT 8093
#

import http.server
import socketserver
from http import HTTPStatus

i = 0

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        global i
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        my_str = 'global var global var  Software Engineering is the process of creating and maintaining computer programs using organized and structured approaches. It involves designing, building, and ensuring the functionality and reliability of software systems. List of different types of Software Engineering: Waterfall Model, Agile Software Development, DevOps, Lean Software Development, Spiral Model, Rapid Application Development (RAD), Big Data Engineering, Embedded Software Engineering, Web Development, Mobile App Development, Game Development, Artificial Intelligence (AI) and Machine Learning (ML) Engineering, Cybersecurity Engineering, Cloud Computing and DevOps, Quality Assurance and Testin :' + str(i)
        i = i+1
        self.wfile.write(bytes(my_str, 'utf-8'))


httpd = socketserver.TCPServer(('', 8093), Handler)
httpd.serve_forever()