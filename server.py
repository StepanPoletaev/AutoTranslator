import socket
from googletrans import Translator

translator = Translator()
server_lang = 'fr'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1337))
server.listen()

client, addr = server.accept()


while True:
    message = client.recv(1024).decode()
    lang = message[1:message.index(']')]
    translation = translator.translate(
        message[message.index(']')+1:],
        src=lang, dest=server_lang
    )
    print(translation.text)

