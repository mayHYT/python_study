#client UDP

import socket

def clientFunc():

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "hello, this is May huang..."

    #发送的数据必须是bytes格式
    data = text.encode()

    #发送
    sock.sendto(data, ("127.0.0.1", 7852))

    data,addr = sock.recvfrom(200)

    data = data.decode()

    print(data)

if __name__ == '__main__':
    clientFunc()