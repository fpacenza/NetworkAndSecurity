#/usr/bin/python3

# sudo pip3 install typer[all] 
# sudo pip3 install rich
# sudo apt install mutt

import subprocess
import os
from time import sleep
import typer
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
console = Console()


def main(ef: str, cf: str, address: str, p: str = ""):

    if (os.path.exists(ef) and os.path.exists(cf)):
        with console.status(f"Hiding {ef} into {cf}..."):
            steghide_args = ["steghide", "embed", "-ef", ef, "-cf", cf, "-p", p]
            steghide = subprocess.Popen(steghide_args, stdout=subprocess.PIPE)
            steghide.communicate()
        console.log(f"[bold green]Hid {ef} into {cf} successfully![/bold green]")

        with console.status(f"Sending email to {address} with attacched {cf}..."):
            echo = subprocess.Popen(["echo", "Steghide email test"], stdout=subprocess.PIPE)
            mutt_output = subprocess.check_output(["mutt", "-s", "Steghide email test", address, "-a", cf], stdin=echo.stdout, stderr=subprocess.PIPE)
            console.log(f"[bold red]Email Sent[/bold red]")
    

if __name__ == "__main__":
    typer.run(main)
