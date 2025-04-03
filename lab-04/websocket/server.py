import random
import tornado.ioloop
import tornado.web
import tornado.websocket

class WebSocketServer(tornado.websocket.WebSocketHandler):
    clients = set()
    def open(self):
        WebSocketServer.clients.add(self)
    def on_close(self):
        WebSocketServer.clients.remove(self)
    @classmethod
    def send_message(cls, message: str):
        print(f"Sending message {message} to {len(cls.clients)} client(s).")
        for client in cls.clients:
            client.write_message(message)
class RandomWordSelector:
    def __init__(self)