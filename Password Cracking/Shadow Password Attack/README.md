# Crack Shadow Hashes on a Linux System

A couple files of particular interest on Linux systems are the `/etc/passwd` and `/etc/shadow` files. 

## `/etc/passwd` File
The `/etc/passwd` file contains basic information about each user account on the system, including the root user which has full administrative rights, system service accounts, and actual users. 
A typical line is composed by 7 different fields and it looks something like this:

`msfadmin:x:1000:1000:msfadmin,,,:/home/msfadmin:/bin/bash`

 1. The first field is the user's login name;
 2. The second field traditionally contained an encrypted password, but nowadays (unless you get extremely lucky) it merely contains the letter "x," to denote that a password has been assigned. If this field is blank, the user does not need to supply a password to log in;
 3. The third field is the user ID, a unique number assigned to the user;
 4. The fourth field is the group ID;
 5. The fifth field is typically the full name of the user, although this can also be left blank;
 6. The sixth field is the user's home directory;
 7. Finally, the seventh field is the default shell, usually set to `/bin/bash`

## `/etc/shadow` File

The `/etc/shadow` file contains the encrypted passwords of users on the system. While the `/etc/passwd` file is typically world-readable, the `/etc/shadow` is only readable by the root account. The shadow file also contains other information such as password expiration dates. A typical line in `/etc/shadow` will look like this:

`msfadmin:$1$XN10Zj2c$Rt/zzCW3mLtUWA.ihZjA5/:14684:0:99999:7:::`


## Cracking the Hashed Password using John the Ripper
### **Prerequisites**
 * The user must obtain a superuser privileges (see `privilege escalation attacks`)
 * Install `John the Ripper`
 
        sudo apt install john
 * Download a good dictionary (e.g., `rockyou`)

        mkdir /usr/share/rockyou
        cd /usr/share/rockyou
        wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt


### **Steps**
 1. First of all we need to make a copy of the `passwd` file and of the `shadow` file. As previosly said, the `shadow` file **\*cannot\*** be *read* by non-superuser thus, the following command must be executed as **root**
        
        sudo cp /etc/passwd /etc/shadow .

 2. To turn an `/etc/shadow` file into a normal unix password file, we must use the `unshadow` utility. Then we can run `John the Ripper` in order to crack user passwords

        umask 077
        sudo unshadow passwd shadow > password.txt

 3. Now you can start cracking **your** password in order to evaluate its security

        john --format=crypt --wordlist=/usr/share/rockyou/rockyou.txt password.txt

 4. `Wait`
 5. Show the results

        sudo john --show password.txt