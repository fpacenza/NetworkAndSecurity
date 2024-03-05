# GNS3 Laboratory Configuration

This guide is useful to setup the GNS3 laboratory in order to be used during the next lab sessions.

We highly recommend to use a Linux/UNIX guest system GNS3 software can be downloaded [here](https://www.gns3.com/software/download)

## GNS3 configuration steps

### Preliminaries
The following images/binaries must be downloaded before starting the configuration
- [Cisco C7200](https://mega.nz/#!RZtA0SwD!XBjqI5Dkrienz7tHaYg601Dwq-ypAqWZv8Ut3mFuKoI) (~45 MB)
- [Cisco C3745](https://mega.nz/#!lR8Q1SpD!5j3lYt9roopuTK6NgHBp9HRM6YP3hq8RiK_nHA7Tktw) (~38 MB)
- [Ubuntu Cloud Host](http://cloud-images.ubuntu.com/releases/focal/release/ubuntu-20.04-server-cloudimg-amd64.img) (~580 MB)
- [Ubuntu Cloud Init Data](https://github.com/asenci/gns3-ubuntu-cloud-init-data/raw/master/ubuntu-cloud-init-data.iso) (~128 KB)
- [Raspberry Pi OS Desktop](https://downloads.raspberrypi.org/rpd_x86/images/rpd_x86-2021-01-12/2021-01-11-raspios-buster-i386.iso) (~3 GB)

## Open Gns3 and create project
- Run GNS3
- Create new project

## Internet Configuration
- Go on the left-bar and select hosts, then drag the appliance *CLOUD* into your project
- Double click on imported appliance
- Check **show special ethernet interfaces** checkbox
- Click on refresh
- Select **virbr0** interface on dropdown

**Attention!** If *virbr0* doesn’t appear in the dropdown menu, you need to install
libvirt on your machine. On Ubuntu linux system, run the following command:
`sudo apt install libvirt0 libvirt-clients libvirt-daemon libvirt-dev`
- Click on add
- Remove your **wireless eth** interface from the table (select your wi-fi interface, then click *delete*)
- Click on OK
- Rename *Cloud* into *InternetAccess* (don’t use spaces for device name)

## Router Configuration
The **Cisco C7200** image will be used as router. Cisco image must be imported into GNS3 using a personalized template

### Import Cisco 7200 image as template in GNS3
- Click on FILE -> New template
- Select **Install an appliance from the GNS3 server (recommended)** then click on *next*
- Type **Cisco 7200** into filter search bar
- Select **Cisco 7200 Dynamips** under the Routers tab and click on install
- Select *install the appliance on your local computer* then click on next
- Check **allow custom files** checkbox
  - If a popup appears, click on **yes**
- Click on **C7200-adventerprisek9-...-124-24.T5...** voice
- Click on import (bottom left corner)
- Select the previously downloaded image of Cisco 7200 and press yes
- Click (again) on **C7200-adventerprisek9-...-124-24.T5...** voice and press next
- Well Done!

### Use the Cisco 7200 appliance on our topology
From now on, the Cisco 7200 router should appears in the available devices inside the hosts section on the left bar
- Drag and drop Cisco 7200 device into GNS3 hierarchy
- Double click on the imported router
  - Go to the Slots tab
  - Replace C7200-IO-FE into dropdown with **C7200-IO-2FE**
- Link **FastEthernet0/0** interface of the Cisco 7200 Router with the **virbr0** interface of the Cloud (InternetAccess) appliance imported before
- Configure the router using a configuration file (router appliance must be stopped)

   - Download Cisco 7200 configuration from course website and open it
      - *Be careful:* File name must be c7200_startup-config.cfg
   - Copy its content
   - Right-click on the router imported in GNS3
   - Click on edit config
   - click on ok if the system asks which config file must be edited
   - Replace the current configuration with the ones copied before
   - Click on SaveSwitch Configuration

### Import Cisco 3745 image as template in GNS3
The Cisco C3745 image will be used as switch
- Click on FILE -> New template
- Select *Install an appliance from the GNS3 server (recommended)* then
click on next
- Type *Cisco 3745* into filter search bar
- Select Cisco 3745 Dynamips under the Routers tab and click on install
- Select install the appliance on your local computer then click on next
- Check allow custom files checkbox
  - If a popup appears, click on yes
- Click on C3745-adventerprisek9-...-124-25d... voice
- Click on import (bottom left corner)
- Select the previously downloaded image of Cisco 3745 and press yes
- Click (again) on C3745-adventerprisek9-...-124-25d... voice and press next
- Well Done!

### Use the Cisco 3745 appliance on our topology
- Drag and drop Cisco 3745 device into GNS3 hierarchy
- Double click on the imported router
- Go to the Slots tab
  - Remove all adapters from **WIC**
  - Remove the adapter on slot 3
  - Replace adapter on slot 2 with **NM-16ESW**
- Link **FastEthernet0/1** interface of *Cisco 7200* to **FastEthernet1/15** interface of **Cisco 3745**
  - **DO NOT USE INTERFACES FASTETHERNET 0/+.** These interfaces are configured for routing. For our purposes we will use interfaces FASTETHERNET 1/* which have been configured for switching
- Configure the router/switch using a configuration file (router/switch appliance must be stopped)
  - Download **Cisco 3745** configuration from course website and open it
    - Be careful: File name must be **c3745_startup-config.cfg**
  - Copy its content
  - Right-click on the router imported in GNS3
  - Click on edit config
  - click on ok if the system asks which config file must be edited
  - Replace the current configuration with the ones copied before
  - Click on SaveHosts Configuration

### Ubuntu Cloud Host
- For our purposes we will use 3 hosts, based on Ubuntu-20.04-server-clouding
- Create a new template as we did for Cisco 7200 router and Cisco 3745 switch
- Click on FILE -> New template
- Select **Install an appliance from the GNS3 server (recommended)**
then click on next
- Type **Ubuntu Cloud Guest** into filter search bar
- Select **Ubuntu Cloud Guest** under the Guests tab and click on install
- Select install the appliance on your local computer then click on
next
- Check **allow custom files** checkbox
  - If a popup appears, click on *yes*
- Click on **ubuntu-cloud-init-data.iso** under **Ubuntu Cloud Guest version 20.04 (LTS)** voice
- Click on import (bottom left corner)
- Select the previously downloaded **ubuntu-cloud-init-data.iso** and press **yes**
- Click on **ubuntu-20.04-server...** under **Ubuntu Cloud Guest version 20.04 (LTS)** voice
- Click on import (bottom left corner)
- Select the previously downloaded ubuntu 20.04 image and press yes
- Click (again) on ubuntu-20.04-server... under Ubuntu Cloud Guest
version 20.04 (LTS) voice and press next
- Well Done!

After that the import is complete, drag and drop 3 times the image into your GNS3 project 

### Raspberry Pi OS Desktop
A Raspberry Pi image will be used as attacker inside our laboratory sessions

#### Import the image
- Install VirtualBox
- Windows users can download the installer [here](https://download.virtualbox.org/virtualbox/6.1.26/VirtualBox-6.1.26-145957-Win.exe)
- LINUX users you can installing using this [guide](https://www.virtualbox.org/wiki/Linux_Downloads). On Ubuntu 22.04 LTS, you can just execute the following command: `sudo apt install virtualbox`

#### Create a new Virtual Machine
- Start VirtualBox
- Click on NEW
- Name: Raspbian
- Type: Linux
- Version: Debian (32-bit)
- Press on create
- File size: 25 GB
- Right click on the new Raspbian machine-
- Go to settings -> storage
- Click on Add optical drive
- Select the previously downloaded image (**2021-01-11-raspios... .iso**)
- Go to network
  - Attached to: Not Attached
  - Press OK
- Double click on the machine to run
  - If a popup appears (select startup disk...), press Run
- Follow the instruction!

### Import the new Raspbian host in GNS3
- Start GNS3
- Go to Edit -> Preference (or use keyboard shortcut CTRL + SHIFT + P)
- Go to VirtualBox VMs and click on New
- Chose the Raspbian VM and check use as a linked base VM (experimental)
- Press Finish
- Click on Edit
- Go to Network tab and click on **Allow GNS3 to use any configured**
VirtualBox adapter
- Click on OK
- Go to QEMU tab
- Deselect both checkboxes for hardware acceleration

### Configuration
- Open GNS3
- Add 1 Raspbian OS in the project
- Add 2 Ubuntu Images in the project
- Connect the first Ubuntu image to the Cisco 3745 **FastEthernet1/0** port
- Connect the second Ubuntu image to the Cisco 3745 **FastEthernet1/1** port
- Connect the Raspbian image to the Cisco 3745 **FastEthernet1/2** port
- Start the GNS3 project
