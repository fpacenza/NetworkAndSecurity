#/usr/bin/python3

# sudo pip3 install typer[all] 
# sudo pip3 install rich

import subprocess
from time import sleep
import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
console = Console()


def main(port: str, listen: bool = False, hostname: str = "localhost", key: str = "key", algorithm: str = "-pbkdf2"):
    openssl_args = ["openssl","enc", "-a", algorithm, "-k", key, "-base64"]
    if listen:
        openssl_args.append("-d")
        netcat = subprocess.Popen(["netcat", "-l", port], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        console.log(f"Server Mode")

        while True:
            out = netcat.stdout.readline()
            if out == '' and netcat.poll() is not None:
                break
            if out:
                console.log(Panel(Text(f"Encrypted string: {out.decode()}", no_wrap=True)))
                with console.status("[bold green]Decrypting string...[/bold green]"):
                    sleep(1)
                    echo = subprocess.Popen(["echo", out.decode()], stdout=subprocess.PIPE)
                    openssl_output = subprocess.check_output(openssl_args, stdin=echo.stdout, stderr=subprocess.PIPE)
                    console.log(f"[italic]Decrypted string:[/italic] [bold red]{openssl_output.decode()}[/bold red]")



    else:
        openssl_args.append("-e")
        netcat = subprocess.Popen(["netcat", hostname, port], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        console.log(f"Client Mode")
        
        while True:
            to_encrypt = input()
            with console.status("[bold green]Encrypting string...[/bold green]"):
                sleep(1)
                echo = subprocess.Popen(["echo", to_encrypt], stdout=subprocess.PIPE)
                openssl_output = subprocess.check_output(openssl_args, stdin=echo.stdout, stderr=subprocess.PIPE)

            console.log(Panel(Text(f"Original string: {to_encrypt}")))
            console.log(f"[italic]Encrypted string:[/italic] [bold red]{openssl_output}[/bold red]")

            with console.status("[bold green]Sending encrypted string...[/bold green]"):
                sleep(1)
                netcat.stdin.write(openssl_output)
                netcat.stdin.flush()



if __name__ == "__main__":
    typer.run(main)
