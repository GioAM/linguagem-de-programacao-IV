import socket, pickle
HOST =''
PORT=5555
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

origem = (HOST, PORT)
tcp.bind(origem)
file_path= "C://teste//"
tcp.listen(2)

while True:
    con, cliente = tcp.accept()
    print('Cliente %s conectado' % str(cliente))

    mensagem = con.recv(1024)
    mensagem = mensagem.decode("UTF-8")

    arquivo = open(file_path + mensagem[0: mensagem.find(".txt") + 4],'w')
    inicio = mensagem.find("inicio") + 6
    fim = mensagem.find("fim")
    arquivo.write(mensagem[inicio:fim])

    arquivo.close()


    print("Cliente %s envio a mensagem; %s" % (str(cliente),mensagem))
