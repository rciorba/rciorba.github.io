import asyncio
import socket


class EchoServer:

    async def run_forever(self, loop):
        server_addr = ('localhost', 6000)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(server_addr)
        sock.setblocking(False)
        sock.listen(8)
        while True:
            con, client_addr = await loop.sock_accept(sock)
            print("{} connected".format(client_addr))
            loop.create_task(self.handle_client(con, loop))

    async def handle_client(self, con, loop):
        while True:
            data = await loop.sock_recv(con, 16)
            if data:
                await loop.sock_sendall(con, data)
            else:
                con.close()
                return

loop = asyncio.get_event_loop()
loop.run_until_complete(EchoServer().run_forever(loop))
