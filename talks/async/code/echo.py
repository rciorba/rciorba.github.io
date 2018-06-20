import socket


class EchoServer:

    def run_forever(self):
        server_addr = ('localhost', 6000)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(server_addr)
        sock.listen(8)
        while True:
            con, client_addr = sock.accept()
            print("{} connected".format(client_addr))
            self.handle_client(con)

    def handle_client(self, con):
        while True:
            data = con.recv(16)
            if data:
                con.sendall(data)
            else:
                con.close()
                return

EchoServer().run_forever()
