import signal
import sys
import threading

class TestServer:
    def __init__ (self, interface, port=8000):
        from wsgiref.simple_server import make_server
        signal.signal(signal.SIGINT, self.sigint_handler)
        self.server = make_server('localhost', port, interface)
        self.server.serve_forever()
    def sigint_handler(self, signal, frame):
        threading.Thread(target=self.server.shutdown).start()
        sys.exit(0)