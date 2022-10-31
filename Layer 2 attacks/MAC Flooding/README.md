# MAC FLOODING

A MAC flooding is a technique employed to compromise the security of network switches. The attack works by forcing legitimate MAC table contents out of the switch and forcing a unicast flooding behavior potentially sending sensitive information to portions of the network where it is not normally intended to go

To execute the full exercise, follow these steps

* Run the GNS3 lab
* Connect to **host_1** and **host_2** using telnet command `telnet localhost <PORT>`
* Execute the `MACFloodingChallengeSender.py <HOST_1_SRC_IP> <HOST_2_DST_IP>` script on **host_1**
* Connect to the **Attacker** host and execute the `mac_flooding.py <NETWORK/NETMASK>` script
* Execute `sudo tshark -Y "udp && ip.dst==<HOST_2_IP>" -T fields -e data > raw-data.txt`  
* Wait some seconds
* Convert the `raw-data.txt` file in **_base64_** `cat raw-data.txt | xxd -r -p > output.txt`
* Open the `output.txt`, find the password and the encryption algorithm
* Use the **openssl enc** to decrypt data `cat output.txt | openssl enc -d -a <CYPHER> -k <PASSWORD_KEY> -base64`

###### Note that, in this exercise, **\<CYPHER\>** value is `-aes-256-cbc` whereas **\<PASSWORD_KEY\>** value is `NS_MacFloodingKey`. We use `pbkdf2` as key derivation function.

