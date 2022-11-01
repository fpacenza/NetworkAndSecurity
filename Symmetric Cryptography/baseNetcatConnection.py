import subprocess
from time import sleep
import typer

def main(port: str, listen: bool = False, hostname: str = "localhost"):
    if listen:
        netcat = subprocess.Popen(["netcat", "-l", port], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="UTF-8")
        while True:
            out = netcat.stdout.readline().strip()
            if out == "" and netcat.poll() is not None:
                break
            print(f"Received from client: {out}")
    else:
        netcat = subprocess.Popen(["netcat", hostname, port], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="UTF-8")
        while True:
            message = input("Input message: ")
            # ATTENTION: if you do not add a \n to your message, your netcat socket will stay in wait before sending the message
            netcat.stdin.write(message + "\n")
            netcat.stdin.flush()

if __name__ == "__main__":
    typer.run(main)
