# MAC FLOODING

A **MAC flooding attack**, also known as **switch flooding**, is a cyber attack technique that exploits vulnerabilities in network switches on switched Local Area Networks (LANs). The attack involves sending a large amount of packets with forged Media Access Control (MAC) addresses to the switch.

## How does a MAC flooding attack work?

1. The attacker bombards the network with packets containing fake MAC addresses.

2. The switch receives these packets and updates its Content Addressable Memory (CAM) table by associating the fake MAC addresses with network ports.

3. The CAM table has a limited capacity to store MAC addresses. When the table fills up, new forged MAC addresses overwrite legitimate ones.

4. The switch, confused about which port certain MAC addresses belong to, goes into `fail open mode`.

5. In `fail open mode`, the switch behaves like a hub, sending all packets to all ports, including the attacker's traffic.

6. Since the attacker is connected to the network, they can intercept and analyze all the traffic flowing through it, potentially including sensitive data and passwords.


## Impacts of a MAC Flooding Attack:

**Service Disruption:** The network becomes unusable or very slow for legitimate users.

**Data Sniffing:** The attacker can intercept and read sensitive data like passwords and financial information.

**Denial-of-Service (DoS):** The attacker can render the network inaccessible to legitimate users.

## How to Defend Against a MAC Flooding Attack:

- Enable MAC flooding protection on your switch.

- Use switches with large CAM tables.
Segment your network into VLANs to limit the attack's impact.

- Implement authentication and encryption techniques to protect your data.

# How to run the exercise

To execute the full exercise, follow these steps

* Run the GNS3 lab
* Connect to **host_1** and **host_2** using telnet command `telnet localhost <PORT>`
* Execute the `MACFloodingChallengeSender.py <HOST_1_SRC_IP> <HOST_2_DST_IP>` script on **host_1**
* Connect to the **Attacker** host and execute the `mac_flooding.py <NETWORK/NETMASK>` script
* Execute `sudo tshark -Y "udp && ip.dst==<HOST_2_IP>" -T fields -e data > raw-data.txt`  
* Wait some seconds
* Convert the `raw-data.txt` file in **_base64_** `cat raw-data.txt | xxd -r -p > output.txt`
* Open the `output.txt`, find the password and the encryption algorithm
* Use the **openssl enc** to decrypt data `cat output.txt | openssl enc -d -a <CYPHER> -pbkdf2 -k <PASSWORD_KEY> -base64`

###### Note that, in this exercise, **\<CYPHER\>** value is `-aes-256-cbc` whereas **\<PASSWORD_KEY\>** value is `NS_MacFloodingKey`. We use `pbkdf2` as key derivation function.

