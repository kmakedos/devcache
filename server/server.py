import socket
import sys

class Server:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = ('localhost', 4000)
        self.cache = {}

    def handle_GET(self, key):
        print(f"Handling GET request for key: {key}")
        if key in self.cache.keys():
            return f"{self.cache[key]}"
        else:
            return "Not Found in Cache"

    def handle_PUT(self, data):
        try:
            key = data.split(':')[0]
            value = data.split(':')[1:]
        except ValueError:
            return "Key:Value not found in data"
        print(f"Handling PUT request for key: {key, value}")
        if not key:
            return "No key found"
        else:
            self.cache[key] = value
            return "OK"

    def handle_connection(self, conn):
        while True:
            data = conn.recv(1024).decode("utf-8").strip()
            print(f"Received {data}")
            if data:
                if data[0:3].upper() == "GET" :
                    ret = self.handle_GET(data[3:])
                    conn.send(ret.encode("utf-8"))
                if data[0:3].upper() == "PUT" :
                    ret = self.handle_PUT(data[3:])
                    conn.send(f"{ret}\n".encode('utf-8'))
            else:
                print("No data received\n")
                break

    def start(self):
        self.sock.bind(self.address)
        self.sock.listen(5)
        while True:
            conn, addr = self.sock.accept()
            try:
                print ('Connection established from {}'.format(addr))
                self.handle_connection(conn)

            finally:
                conn.close()





