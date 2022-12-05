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

echo "Creating new network interface $1:0"
ifconfig $1:0 192.168.2.2 pointopoint 192.168.2.1 up

echo "Adding new static entry in the ARP table $1:0"
sudo arp -sD 192.168.2.1 $1 pub

echo "Check the arp table (if nothing appears try to manually add a static entry)"
arp -n | grep "192.168.2.1"

echo "Trying to ping the point-to-point host"
ping -c 5 192.168.2.1

echo "Configuration complete!"

echo "Remember to start a new ssh connection as *superuser*
    sudo ssh user@192.168.2.1 -w 0:0"
