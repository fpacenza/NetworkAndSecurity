#!/usr/bin/python3
import http.client
import typer
from rich.console import Console
console = Console()

def main(website: str = "www.google.com"):
    c = http.client.HTTPSConnection(website)
    c.request("GET", "/")
    response = c.getresponse()
    console.log(response.status, response.reason)
    data = response.read()
    console.log(data)

if __name__ == "__main__":
    typer.run(main)