# Crack SAM Hashed Password on a Windows System
The **S**ecurity **A**ccounts **M**anager **(SAM)** is a database file in the Microsoft Windows operating system that contains usernames and passwords.

The primary purpose of the SAM is to make the system more secure and protect from a data breach in case the system is stolen. The SAM is available in different versions of Windows, starting from Windows XP to Windows 11.

Password and user list can be found in the following registry key
    
    HKLM\SAM
    HKLM\SYSTEM

## Cracking Windows Password
### **Prerequisites**
 * The user must obtain a superuser privileges (see `privilege escalation attacks`)
 * Disable Windows Defender
 * Download the following software
   * [`Mimikatz`](https://github.com/gentilkiwi/mimikatz/releases/download/2.2.0-20210810-2/mimikatz_trunk.zip)
   * [`OphCrack`](https://sourceforge.net/projects/ophcrack/files/ophcrack/3.8.0/ophcrack-3.8.0-bin.zip/download)
   * [`OphCrack Tables`](http://sourceforge.net/projects/ophcrack/files/tables/Vista%20proba%20free/vista_proba_free.zip/download)


### **Steps**
 1. Dump the SAM files

     1.1. Open a `PowerShell` as admin and execute the following commands

        reg save HKLM\SAM sam.bkp
        reg save HKLM\SYSTEM sys.bkp
 2. Extract hashes

    2.1. From the `PowerShell` as admin execute the following commands

        mimikatz.exe
        privilege::debug
        token::elevate
        log hash.log
        lsadump::sam sys.bkp sam.bkp
    
    2.2. Open file `hash.txt` and look for users you want to test password security
    
    2.3. Extract the following user informatiion
              
        Username
        User ID (optional)
        Hash NTLM
    
    2.4. Go to the `ophcrack/x64` folder
    
    2.5. Create a file named `users.txt` and paste the following information

        Username:User_ID::Hash_NTLM:::
    2.6. `users.txt` file example in which the `User_ID` field is empty

        francesco:::57158936eqke28fho38fuw74y9fwnplas:::

 3. Crack the password
 
    3.1. Start `ophcrack.exe` as admin

    3.2. Click on `load --> PWDUMP` and select the `users.txt` file

    ![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/SAM%20Password%20Attack/1.ophcrack_load.png?raw=true)

    3.3. Click on `tables` and select the previously downloaded `vista probabilistic free` table **folder**
    
    ![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/SAM%20Password%20Attack/3.ophcrack_crack.png?raw=true)

    3.4. Click on `crack` and wait until the end

    ![alt text](https://github.com/fpacenza/NetworkAndSecurity/blob/main/SAM%20Password%20Attack/3.ophcrack_crack.png?raw=true)