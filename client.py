import socket
import sys

def main():
    # TCP/IPソケットの作成
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # サーバが待ち受けているポートにソケットを接続します
    server_address = './socket_file'
    print('connecting to {}'.format(server_address))

    try:
        sock.connect(server_address)
        print('Connected')
    except socket.error as err:
        print(err)
        sys.exit(1)

    while True:
        # データ送信
        message = input("> ")
        sock.sendall(message.encode("utf-8"))

        # データ受信
        data = sock.recv(1024)
        data_str = data.decode('utf-8')
        print('From server: ' + data_str)

        if message == "exit":
            sock.close()
            print('closing socket')
            break


if __name__ == '__main__':
    main()