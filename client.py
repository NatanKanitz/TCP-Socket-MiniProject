from socket import *

PORTA = 2000

# cria socket TCP em IPv4
s = socket(AF_INET, SOCK_STREAM)

# conectando ao servidor
enderIP = gethostbyname('localhost')
s.connect((enderIP, PORTA))

while True:
    frase = input("\n Peça uma informação ao servidor:\n")

    if frase.lower() == "fim":
        break
    s.send(frase.encode()) #converte para tipo bytes

    msg = s.recv(4096)
    print(msg.decode("utf-8"))

s.close()
