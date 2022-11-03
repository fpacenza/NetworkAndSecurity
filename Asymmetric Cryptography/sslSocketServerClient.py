#!/usr/bin/python3
import socket
import ssl
import typer
from rich.console import Console
import os
import certifi
console = Console()

def tls_server(server_socket, SERVER_HOST: str, SERVER_PORT: int):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert/fullchain.pem', 'cert/privkey.pem')
    
    server_socket = context.wrap_socket(server_socket, server_side=True)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(0)

    while True:
        connection, client_address = server_socket.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            console.log("Received: %s" % (data.decode('utf-8')))

def tls_client(client_socket, SERVER_HOST: str, SERVER_PORT: int, CLIENT_HOST: str, CLIENT_PORT: int):
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations(cafile=os.path.relpath(certifi.where()),capath=None,cadata=None);
    #context.load_cert_chain('cert/cert.pem', 'cert/privkey.pem')

    client_socket = context.wrap_socket(client_socket, server_hostname="networksecurity.site")
    client_socket.bind((CLIENT_HOST, CLIENT_PORT))
    client_socket.connect((SERVER_HOST, SERVER_PORT))

    while True:
        from time import sleep
        console.log("Message to encrypt: ")
        message = input()
        client_socket.send(message.encode("utf-8"))
        sleep(1)
    

def main(server: bool=False, SERVER_HOST: str="127.0.0.1", SERVER_PORT: int=60000, CLIENT_HOST: str="127.0.0.1", CLIENT_PORT: int=60002):
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if server:
        tls_server(my_socket, SERVER_HOST, SERVER_PORT)
    else:
        tls_client(my_socket, SERVER_HOST, SERVER_PORT, CLIENT_HOST, CLIENT_PORT)


if __name__ == "__main__":
    typer.run(main)