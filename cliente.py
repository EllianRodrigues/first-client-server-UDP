from socket import socket, AF_INET, SOCK_DGRAM  #Criar Socket
mClientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddress = ('localhost', 10112)

for i in range(3): #Loop para o cliente enviar n mensagens
    
    message = input('Enter the request: ') # menssage para ser enviar
    mClientSocket.sendto(message.encode(), serverAddress) # enviando...
    
    data, sAddress = mClientSocket.recvfrom(2048) #recebendo
    reply = data.decode()
    print(f'Response received: {reply}') # Printando

mClientSocket.close()