import socket

# Crea un socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta el socket a la dirección del servidor y al puerto 65432
server_address = ('localhost', 65432)
print('Conectando a {} puerto {}'.format(*server_address))
sock.connect(server_address)

try:
    # Enviar datos
    message = b'Este es el mensaje. Sera repetido.'
    print('Enviando {!r}'.format(message))
    sock.sendall(message)

    # Esperar la respuesta
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print('Recibido {!r}'.format(data))

finally:
    print('Cerrando socket')
    sock.close()
