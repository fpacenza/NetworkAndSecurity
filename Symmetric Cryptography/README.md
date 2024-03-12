# Symmetric Cryptography

Symmetric-key algorithms are algorithms for cryptography that use the same cryptographic keys for both the encryption of plaintext and the decryption of ciphertext. The keys may be identical, or there may be a simple transformation to go between the two keys. The keys, in practice, represent a shared secret between two or more parties that can be used to maintain a private information link.

In order to run all the scripts, the following 2 Python3 modules must be installed:
 * `sudo pip3 install typer[all] rich`

## Base Netcat connection using `subprocess` module in Python3
Download the `baseNetcatConnection.py` script in order to understand how to use subprocess library to execute Netcat via python3. 
## Cryptocat
`cryptocat.py` is a Python script able to add encryption and decryption functionalities to the standard `netcat` linux command. Encryption and decryption are performed using the `openssl enc` command

In order to execute the script follow these steps:
 * Run the `cryptocat.py` script in **server mode**: `python3 cryptocat.py --listen <PORT> --key mypassword --algorithm -aes-256-cbc`
 * Run the `cryptocat.py` script in **client mode**: `python3 cryptocat.py <PORT> --key mypassword --algorithm -aes-256-cbc`
 * **BE CAREFUL:** password and decrypt algorithm **have to be** the same in server and client mode
 * Type some text in client console

 ### How to use `openssl enc` command via examples
 1. **Encrypt and decrypt a file:**:
    * **Encrypt:**
    
          openssl enc -e --algorithm -aes-256-cbc -k mysecretkey -pbkdf2 -base64 -in plaintext_file.txt -out crypted_file.txt

    * **Decrypt:**
    
          openssl enc -d --algorithm -aes-256-cbc -k mysecretkey -pbkdf2 -base64 -in crypted_file.txt -out plaintext_file.txt

 2. **Encrypt and decrypt text via STDIN and show the result via STDOUT:**
    * **Encrypt:**
    
          echo "Hello" | openssl enc -e --algorithm -aes-256-cbc -k mysecretkey -pbkdf2 -base64

    * **Decrypt:**
    
          echo "U2FsdGVkX19gId+esKSi4m118OEiotwCH4tjaaMvCvM=" | openssl enc -d --algorithm -aes-256-cbc -k mysecretkey -pbkdf2 -base64




 ## Smutt
`smutt.py` is a Python script able to hide a file inside an image and send the output image as attachment using mutt service

In order to execute the script follow these steps:
 * Install and configure `mutt` service on your laptop `sudo apt install mutt`
 * Install `steghide` command `sudo apt install steghide`
 * Run the `smutt.py` script
 * `python3 smutt.py <path/to/file/to/embed> <path/to/image.jpg> output.jpg <your_email@domain.com> --pwd pass`
