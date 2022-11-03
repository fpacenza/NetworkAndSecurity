# Asymmetric Cryptography

Asymmetric-key algorithms work in a similar manner to symmetric-key algorithms, where plaintext is combined with a key, input to an algorithm, and outputs ciphertext. The major difference is the keys used for the encryption and decryption portions are different, thus the asymmetry of the algorithm. The key pair is comprised of a **private key** and a **public key**. As the names imply, the public key is made available to everyone, whereas the private key is kept secret. Which key is used for encryption and which key is used for decryption varies depending on the intended use of asymmetric-key algorithm in question.

The two main uses of asymmetric-key algorithms are public-key encryption and digital signatures.

In order to run all the scripts included in this folder, the following 2 Python3 modules must be installed:
 * `sudo pip3 install typer[all] rich`

## HTTPS Client Connection Basic
Download the `httpsClientBasic.py` script in order to understand how to use the necessary modules to perform a simple **http** request over **SSL** or **TLS**

## HTTPS Client Connection Advanced
`httpsClientAdvanced.py` script allows the user to contact a web-server over TLS on port 443. The client creates an SSLContext instance by specifying the highest TLS protocol, then it loads the CA certificates and validates the peer's certificate. Some related information are printed on console.

In order to execute the script follow these steps:
 * Run the `httpsClientAdvanced.py` script: `python3 httpsClientAdvanced.py --url "google.com"`

 ## SSL/TLS Socket Client and Server
`tlsSocketClientServer.py` script is able to create a secure socket server/client in order to allow crypted message exchange.  

In order to execute the script follow these steps:
 * Run the socket server `python3 tlsSocketClientServer.py --server`
    * If necessary you can specify different `SERVER_HOST` address or `SERVER_PORT` through the optional argument
<br/>
    `SERVER_HOST` (default="127.0.0.1")<br/>
    `SERVER_PORT` (default=60000) 
 * Run the socket server `python3 tlsSocketClientServer.py --server`
     * If necessary you can specify different `CLIENT_HOST` address or `CLIENT_PORT` through the optional argument<br/>
    `CLIENT_HOST` (default="127.0.0.1")<br/>
    `CLIENT_PORT` (default=60002) 