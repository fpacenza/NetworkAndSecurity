#!/usr/bin/python3

# sudo pip3 install typer[all] 
# sudo pip3 install rich
# sudo apt install mutt

import subprocess
import os
import typer
from rich.console import Console
console = Console()


def main(ef: str, cf: str, sf: str, address: str, pwd: str = ""):

    if (os.path.exists(ef) and os.path.exists(cf)):
        with console.status(f"Hiding {ef} into {cf}..."):
            steghide_args = ["steghide", "embed", "-ef", ef, "-cf", cf, "-sf", sf, "-p", pwd]
            steghide = subprocess.Popen(steghide_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            steghide.communicate()
        console.log(f"[bold green]{ef} hidden into {cf} successfully. New image written in {sf}![/bold green]")

        with console.status(f"Sending email to {address} with attacched {sf}..."):
            echo = subprocess.Popen(["echo", "Steghide email test"], stdout=subprocess.PIPE)
            subprocess.check_output(["mutt", "-s", "Steghide email test", address, "-a", sf], stdin=echo.stdout, stderr=subprocess.PIPE)
            console.log(f"[bold red]Email Sent[/bold red]")
    

if __name__ == "__main__":
    typer.run(main)
