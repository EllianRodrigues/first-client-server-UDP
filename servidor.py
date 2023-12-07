from socket import socket, AF_INET, SOCK_DGRAM  # criando socket
from threading import Thread

def Threads(socket_do_cliente): # threand para suportar n requisições
    for j in range(3):
        message, endereco_cliente = socket_servidor.recvfrom(2048) # recebendo menssagem
        recebido = message.decode()
        
        print(f'Request received from {endereco_cliente}!\nA Request: {recebido}') #printando menssagem
         
        resposta = 'Hi, client! Request accepted!' #mandando menssagem
        socket_do_cliente.sendto(resposta.encode(), endereco_cliente)

socket_servidor = socket(AF_INET, SOCK_DGRAM) # socket do servidor
socket_servidor.bind(('localhost', 10112)) #
print('server is ready') #

for i in range(2): # aguentar até n clientes
    Thread(target=Threads, args=(socket_servidor,)).start()

