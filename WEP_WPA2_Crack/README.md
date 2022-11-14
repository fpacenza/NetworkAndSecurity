# WEP and WPA Password Cracking
To successfully crack WEP/WPA, you first need to be able to set your wireless network card in "monitor" mode to passively capture packets without being associated with a network.

One of the best tool/suite which can be used to **assess** WiFi Network security is [Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng).

[Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) is a complete suite of tools to assess WiFi network security.

It focuses on different areas of WiFi security:
 * Monitoring: Packet capture and export of data to text files for further processing by third party tools.
 * Attacking: Replay attacks, deauthentication, fake access points and others via packet injection.
 * Testing: Checking WiFi cards and driver capabilities (capture and injection).
 * Cracking: WEP and WPA PSK (WPA 1 and 2).

## Prerequisites
Install the `aircrack-ng` suite
 * `sudo apt install aircrack-ng`

# Crack WEP Password
## How WEP works
Generally WEP encryption works between wireless AP and wireless station (host). First of all, the **host** and the **AP** share their secret key which we commonly call as passphrase.

![alt text](https://vocal.com/wp-content/uploads/2012/05/wep_fig1.gif)

 1. The **host** sends an authentication request to the **AP**. In this step no data encryption takes place

 2. The **AP** responds with an authentication response message consist of challenge text

 3. Now the client uses its secret WEP key to encrypt the challenge text and sends it to the access access point

 4. If the access point successfully decrypt the encrypted challenge and retrieve the original challenge text then it comes to know that the client is also using the same secret key. So responds with an **Confirmation Success** message

 5. Finally, data transfer takes place


# READ WIFI NETWORK INTERFACE DATA

 1. Authenticate a superuser
 2. Execute `iw` command in order to find and manipulate your wireless devices and their configuration 
```
sudo su 
iw dev
```
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WEP/1.%20iw%20dev.png?raw=true)

# START CRACKING

 * The first thing we have to do is to set our network card in *monitor mode* which allows to monitor all traffic received on a wireless channel
    * `airmon-ng start <INTERFACE_NAME>`
 * Check again your network wireless card name using `iw dev` command
     * `iw dev`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WEP/2.%20iw%20dev.png?raw=true)
 * Let's now start `airodump-ng` in order to obtain some useful information about `AP Name`, `Channel` and `BSSID`
    * `airodump-ng <INTERFACE_NAME_MONITOR_MODE>`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WEP/3.%20airodump-ng.png?raw=true)
 * We can now start capturing some data using (again) `airodump-ng` command
 * `airodump-ng -c <NUM_CHANNEL> --bssid <AP_MAC_ADDRESS> -w <OUTPUT_FILE_CAPTURE> <INTERFACE_NAME_MONITOR_MODE>`
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WEP/4.%20airodump-ng%20capture.png?raw=true)

## Start cracking the network password

 * If we need to receive more traffic, we can use `aireplay-ng` command which allows us to send `ARP` requests from hosts to th AP. This utility will trigger traffic through AP giving us the right amount of **Initialization Vector (IV)** in order to retrieve the password.
    * `aireplay-ng -3 <INTERFACE_NAME_MONITOR_MODE> -b <AP_MAC_ADDRESS>`
 * Meanwhile, in another terminal, we can run `aircrack-ng` (as superuser) in order to decrypt the network password
    * `aircrack-ng <OUTPUT_FILE_CAPTURE> `
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/WEP_WPA2_Crack/WEP/5.%20cracking.png?raw=true)

## STOP MONITOR MODE

Remember to disable the **monitor mode** from your wireless network card
 * `airmon-ng stop <INTERFACE_NAME>`