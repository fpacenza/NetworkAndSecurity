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
* Choose the IP and MAC address of the machine you want to attack (we will choose the ip address of the **ubuntu-1 host** for simplicity)
* Execute the `ip_spoofer.py` script as superuser

        sudo python3 ip_spoofer.py <Victim_IP_ADDRESS>
* Connect again to **R1** and check the current IP/MAC assignment using the followng command

        show ip arp
* The pair `<ip,mac>` related to the ip address of our **Victim** has been changed
* Connect to another **ubuntu host machine** (ubuntu-2, for example) and run the following command

        ping <Victim_IP_ADDRESS>
* Execute **Wireshark** on the link which connects the **Victim** machine to the **Switch (SW1)**
    * Check if the **Victim** is receiving new **icmp** requests
* Execute **Wireshark** on the link which connects the **Attacker** machine to the **Switch (SW1)**
    * Check if the **Attacker** is receiving new **icmp** requests
  
