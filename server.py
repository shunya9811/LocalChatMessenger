import os 
import socket
import faker

def main():
    fake = faker.Faker('jp-JP')
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    server_address = './socket_file'

    # ファイルが既に存在しないことを確認する
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    # ソケットをアドレスに紐付ける 
    print('Starting up on {}'.format(server_address))
    sock.bind(server_address)

    sock.listen(1)

    while True:
        connection, client_address = sock.accept()
        
        try:
            print('connection from', client_address)

            while True:
                # データの受信
                data = connection.recv(1024)
                data_str =  data.decode('utf-8')
                print('From Client: ' + data_str)
                
                if data:
                    # データの送信
                    # Fakerを使ってメッセージを生成して、現在のクライアントに送る
                    
                    # Todo: 送られて来たデータを元に、Fakerを使って自然言語処理をするAIを作る
                    degree = fake.job()
                    theme = fake.company()

                    response = "\nイェェェェイ!\n空前絶後のぉ、超絶怒涛の" + degree + "!\n" + theme + "を愛し、" + theme + "に愛された男!\n全ての" + theme + "の生みの親!\nそう、我こそはぁぁ 最強無敵の" + degree + "!\nあまりの" + theme + "でのポテンシャルの高さに" + fake.name() + "から命を狙われてる男ー！\nそう、この俺はぁぁぁ身長180cm、体重70kg、貯金残高500万円、\nキャッシュカードの暗証番号8931、財布は今、楽屋に置いてあります。\n" + fake.name() + "さん、今がチャンスです。\nもう一度言います。ハクサイって覚えてください!\n全てをさらけ出したこの俺はぁぁサンシャイーン、ボコッ" + fake.name() + "!!\nイェェェェェェェェェェェェェェェェイ!!"

                    connection.sendall(response.encode())
                else:
                    print('no data from', client_address)
                    break

        finally:
            # 接続のクリーンアップ
            print("Closing current connection")
            connection.close()

if __name__ == '__main__':
    main()
