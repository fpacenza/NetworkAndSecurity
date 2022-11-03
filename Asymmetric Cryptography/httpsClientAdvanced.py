#!/usr/bin/python3

import socket
import ssl
import os
import certifi
import typer
from rich.console import Console
console = Console()

def main(url: str = "informatica.unical.it"):
    # Create an SSLContext instance by specifying the highest TLS protocol
    # that both the client and the server supports
    sslSettings = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT);
    sslSettings.verify_mode = ssl.CERT_REQUIRED;
    
    # Load the CA certificates used for validating the peer's certificate
    sslSettings.load_verify_locations(cafile=os.path.relpath(certifi.where()),capath=None,cadata=None);

    # Create a connection oriented socket
    con_socket = socket.socket();
    
    # Make SSLSocket from the connection oriented socket
    sslSocket  = sslSettings.wrap_socket(con_socket, server_hostname=url);
    con_socket.close();
    
    # Connect to a server using TLS
    sslSocket.connect((url, 443));
    
    console.log("SSLContext object: %s" % (sslSettings));
    
    # Get the context from SSLSocket and print
    context = sslSocket.context;
    console.log("SSLContext object obtained from SSLSocket: %s" % (context));
    console.log("The type of the secure socket created: %s" % (sslSocket.context.sslsocket_class));
    console.log("Maximum version of the TLS: %s" % (sslSocket.context.maximum_version));
    console.log("Minimum version of the TLS: %s" % (sslSocket.context.minimum_version));
    console.log("SSL options enabled in the context object: %s" % (sslSocket.context.options));
    console.log("Protocol set in the context: %s" % (sslSocket.context.protocol));
    console.log("Verify flags for certificates: %s" % (sslSocket.context.verify_flags));
    console.log("Verification mode(how to validate peer's certificate and handle failures if any): %s" % (sslSocket.context.verify_mode));
    
    # Do SSL shutdown handshake
    sslSocket.unwrap();
    
    # Close the SSLSocket instance
    sslSocket.close();



if __name__ == "__main__":
    typer.run(main)