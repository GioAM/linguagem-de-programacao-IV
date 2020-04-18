import socket, os

host = '192.168.1.123'
port = 5555

file_path = "C://teste"

arquivos = os.listdir(file_path)
destino = (host, port)
for arquivo_nome in arquivos:
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.connect(destino)
    tcp.send(str.encode(arquivo_nome))
    tcp.send(str.encode("inicio"))
    arquivo = open(file_path + f"{arquivo_nome}")
    texto = arquivo.read(1024)
    tcp.send(str.encode(texto))
    arquivo.close()
    tcp.send(str.encode("fim"))
    tcp.close()