import socketserver
import sys
import base64
import traceback
import threading
from . import CommsManager
import numpy as np

class mySocketServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class RobotSocketServer:
    def start(self, port):

        self.server = mySocketServer(('', port), CommsManager.CommsManager) 
        server_thread = threading.Thread(target=self.server.serve_forever)
        # Exit the server thread when the main thread terminates
        server_thread.daemon = True
        server_thread.start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()