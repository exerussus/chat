from Socket import Socket
import threading


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.users = []

    def set_up(self):
        self.bind(('192.168.1.212', 1534))
        self.listen(5)
        self.accept_sockets()

    def send_data(self, data):
        for i in self.users:
            i.send(data)

    def listen_socket(self, listened_socket=None):
        print('Listening user')
        while True:
            data = listened_socket.recv(2048)
            print(f' sent {data.decode("utf-8")}')
            self.send_data(data)

    def accept_sockets(self):
        while True:
            user, address = self.accept()
            print(f'User {address[0]} connected!')
            self.users.append(user)
            listen_accepted_user = threading.Thread(
                target=self.listen_socket,
                args=(user,)
            )
            listen_accepted_user.start()

            # messages


if __name__ == '__main__':
    server = Server()
    server.set_up()
