from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
import cgi
import os
import sys
sys.path.insert(0, "robot")
import robot

robot = robot.robot()

f = 0
b = 0
r = 0
l = 0

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        print self.path
        print parse_qs(self.path[2:])

        file = open("index.html", "r")
        page = file.read()
        file.close()

        self.wfile.write(page)
    def do_POST(self):

        global f
        global b
        global r
        global l
        global robot

        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        
        print form.getvalue("forward")
        print form.getvalue("backward")
        print form.getvalue("left")
        print form.getvalue("right")

        if form.getvalue("forward") == "Forward":
            if f == 0:
                robot.stop()
                robot.forward()
                f = 1
            else:
                robot.stop()
                f = 0
        if form.getvalue("backward") == "Backward":
            if b == 0:
                robot.stop()
                robot.backward()
                b = 1
            else:
                robot.stop()
                b = 0
        if form.getvalue("left") == "Left":
            if l == 0:
                robot.stop()
                robot.left()
                l = 1
            else:
                robot.stop()
                l = 0
        if form.getvalue("right") == "Right":
            if r == 0:
                robot.stop()
                robot.right()
                r = 1
            else:
                robot.stop()
                r = 0

        file = open("index.html", "r")
        page = file.read()
        file.close()

        self.wfile.write(page)

def run(server_class=HTTPServer, handler_class=GP, port=8080):
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:8080...'
    httpd.serve_forever()

run()