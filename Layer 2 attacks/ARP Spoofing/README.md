# ARP SPOOFING

An **ARP spoofing attack**, also known as **ARP poisoning**, is a cyber attack technique that exploits a weakness in the `Address Resolution Protocol (ARP)` to trick devices on a Local Area Network (LAN). The attacker sends fake ARP packets to associate their own Media Access Control (MAC) address with the IP address of another device, such as a router or server.

## How does Arp Spoofing attack works?

1. The attacker broadcasts fake ARP packets to all devices on the network.

2. These forged ARP packets claim that the attacker's MAC address belongs to the IP address of a legitimate device, like the router.

3. Devices on the network receive these fake packets and update their ARP tables with the incorrect association.

4. When a device on the network tries to communicate with the legitimate device (e.g., the router), its traffic gets mistakenly directed to the attacker.

5. The attacker, positioned as a `man-in-the-middle`, can intercept, read, and alter the traffic flowing through them.

## Impacts of an ARP Spoofing Attack:

**Data Interception:** The attacker can steal sensitive data like passwords, financial information, and private communications.

**Data Modification:** The attacker can tamper with the content of packets, potentially redirecting traffic to malicious websites.

**Denial-of-Service (DoS):** The attacker can prevent devices from communicating with the legitimate device, blocking access to resources and services.

## How to Defend Against an ARP Spoofing Attack:

- Use antivirus and firewall software with ARP spoofing protection.

- Enable 802.1X authentication on your network.

- Utilize switches with ARP inspection capabilities.

- Configure static ARP entries for critical devices manually.

# How to run the exercise
To execute the full exercise, follow these steps

* Run the GNS3 lab
* Connect to **host_1** and **host_2** using telnet command `telnet localhost <PORT>`
* Execute the `ARPSpoofingChallengeSender.py <HOST_1_SRC_IP> <HOST_2_DST_IP>` script on **host_1**
* Connect to the **Attacker** host and execute the `arp_spoofer.py <HOST_2_MAC> <HOST_2_SRC_IP>` script
* Execute `sudo tshark -Y "udp && ip.dst==<HOST_2_IP>" -T fields -e data > raw-data.txt`  
* Wait some seconds
* Convert the `raw-data.txt` file in **_base64_** `cat raw-data.txt | xxd -r -p > output.txt`
* Open the `output.txt`, find the password and the encryption algorithm
* Use the **openssl enc** to decrypt data `cat output.txt | openssl enc -d -a <CYPHER> -pbkdf2 -k <PASSWORD_KEY> -base64`




###### Note that, in this exercise, **\<CYPHER\>** value is `-aes-256-cbc` whereas **\<PASSWORD_KEY\>** value is `NS_ArpSpoofingPassword`. We use `pbkdf2` as key derivation function.
