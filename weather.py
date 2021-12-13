import socket
import json #JavaScript Object Notation

city = 'florianopolis'
api_key = 'a94ddad96babc923ce0e550c66b12b21' # chave de acesso
server = 'api.openweathermap.org'
url = '/data/2.5/weather?q={}&appid={}&units=metric&lang=pt_br'.format(city, api_key)
port = 80

request = "GET " + url + " HTTP/1.0\nHost: " + server + "\n\n" # monta o request de modo que o servidor entenda
request_bytes = str.encode(request) # converte a string em bytes

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # cria socket TCP em IPv4
clientSocket.connect((server, port))
clientSocket.send(request_bytes)

result = clientSocket.recv(4096).decode("utf-8")
data = json.loads(result.split("\r\n\r\n")[1])

weatherDescription = data["weather"][0]["description"]
temperature = data["main"]
city = data["name"]

# print(data)

response = {'clima': "Olá, o clima em {} é {}".format(city, weatherDescription),
'temperatura': "Olá, a temperatura em {} é de {}ºC, com mínima de {}ºC e máxima de {}ºC".format(city, temperature["temp"], temperature["temp_min"], temperature["temp_max"])}
##########

# socket servidor

PORTA = 2000

# cria socket TCP em IPv4
serverSocket = socket.socket()

serverSocket.bind(('', PORTA))
serverSocket.listen(5) # num. max de 5 conexoes TCP

while True:
    individualSocket, addr = serverSocket.accept() # aceita conexao com cliente e cria o socket 'c' para conversar com o cliente e armazena o endereco do cliente (IP e numero do socket)

    print('Conectou-se com o endereço {}'.format(addr))

    topico = individualSocket.recv(1024).decode("utf-8").lower()

    while topico != "fim":
        print("Cliente requeriu informações sobre {}".format(topico))
        try:
            if topico in response:
                individualSocket.send(str.encode(response[topico]))
            else:
                individualSocket.send(str.encode("Tópico não disponível"))
        except: #captura erro SIGPIPE (quando o servidor envia mensagem ao cliente apos o socket do cliente ser fechado)
            print("Cliente desconectou")
            break

        topico = individualSocket.recv(1024).decode("utf-8").lower()

    individualSocket.close()
