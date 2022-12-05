#!/bin/sh

# This script must be executed with superuser privileges
if [ $(id -u) -ne 0 ]
  then echo "Please run as root"
  exit
fi

if [ -z "$1" ]
  then echo "Please input an network interface name"
  exit
fi

out=$(ip a s $1)
if [ "$out" = "Device \"$1\" does not exist.\n" ]
    then exit
fi

# Drop all forwarded packets
iptables -P FORWARD DROP

# Accept all packets from the interface $1
iptables -I FORWARD -i $1 -j ACCEPT

# Accept all packets with state ESTABLISHED,RELATED
iptables -I FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# Accept all packet with input and output interface $1:0
iptables -I FORWARD -i $1:0 -j ACCEPT
iptables -I FORWARD -o $1:0 -j ACCEPT

echo "Creating new network interface $1:0"
ifconfig $1:0 192.168.2.1
echo "Configuration complete!"
echo "Remember to set:
 PermitTunnel yes
 AllowAgentForwarding yes
 AllowTcpForwarding yes
into /etc/ssh/sshd_config file"