# VPN using an SSH point-to-point tunneling
A **V**irtual **P**rivate **N**etwork (**VPN**) extends a private network across a public network and enables users to send and receive data across shared or public networks as if their computing devices were directly connected to the private network. The benefits of a VPN include increases in functionality, security, and management of the private network. It provides access to resources that are inaccessible on the public network and is typically used for remote workers. Encryption is common, although not an inherent part of a VPN connection.

A VPN is created by establishing a virtual **point-to-point** connection through the use of dedicated circuits or with tunneling protocols over existing networks. From a user perspective, the resources available within the private network can be accessed remotely

## VPN server and client configuration
### **Goal**
In this session, our goal is to setup a vpn connection from server and client side.

### **Settings**
Work in group with another collegue in order to work on your own laptop (avoiding GNS3 lab)
 * **Server:** you
 * **Client:** your collegue
 * **Router:** you can use your phone. For our exercise, both the **VPN Server** and the **VPN Client** must be connected to the same network

### **VPN Server configuration steps** 
 1. Setup the firewall

        # Drop all forwarded packets
        iptables -P FORWARD DROP
        
        # Accept all packets from the interface $1
        iptables -I FORWARD -i $1 -j ACCEPT
        
        # Accept all packets with state ESTABLISHED,RELATED
        iptables -I FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
        
        # Accept all packet with input and output interface $1:0
        iptables -I FORWARD -i $1:0 -j ACCEPT
        iptables -I FORWARD -o $1:0 -j ACCEPT
 2. Starting the ssh client
       
        sudo service ssh start

 3. Check if the ssh client has been started

        sudo netstat –tpln | grep 22
 
 4. Ensure that the *root* password is set
        
        sudo passwd
    * Insert a new root password

 5. Check incoming connection on the server
 
        sudo tail -f /var/log/auth.log
 6. Enable SSH Tunneling in the ssh configuration file

        sudo pico /etc/ssh/sshd_config

 7. Add or edit the following lines

        PermitTunnel yes
        AllowAgentForwarding yes
        AllowTcpForwarding yes

 8. Restart SSH server
        
        sudo service ssh restart
 
 9. Enable virtual interface

        sudo ifconfig eth0:0 192.168.2.1

### **VPN Client configuration steps** 

 1. Configure a new virtual interface

        sudo ifconfig eth0:0 192.168.2.2 pointopoint 192.168.2.1 up
 2. Check if the other end of the tunnel is reachable using ping command
        
        ping -n 192.168.2.1

 3. Add a new static public entry in the ARP table on the network interface eth0
       
        sudo arp –sD 192.168.2.1 eth0 pub
 
 4. Check the arp table

        arp -n
 
 5. Start the VPN connection
        
        sudo ssh user@192.168.2.1 -w 0:0

### **Check the configuration**
In order to check the vpn configuration start **Wireshark** and have a look to data transferred from server to client (and viceversa)