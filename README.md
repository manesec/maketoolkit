# maketoolkit

Quick to install some pen-testing tools on python and debian like os.

![Logo](Picture/main.png)

# Warning

This is **BETA** version, which mean it need to very unstable, if you find a bug just feel free to submit the issue. you need to update before to use.

## Install

```bash
git clone https://github.com/manesec/maketoolkit.git
cd maketoolkit; chmod u+x *.sh; sudo ./install.sh
```

**Note**: All tools will be locate in `/var/lib/mkt/Tools/Source` which soft link to `/Tools`.

## Update

Just type `sudo mkt-update` to update the tools, **all tools will be delete it and reinstall the source**.

## Usage

```bash
# Update mkt tools and the source just type:
sudo mkt-update

# Install the tools, you can type tools name: 
sudo mkt install Windows/WinPEAS

# Or, goto /Tools/Linux and :
sudo mkt install LinPEAS.mkt

# Before you need to search, you need to install search db.
sudo mkt db install HackTricks

# If you want to support to view .md file, you need to:
sudo mkt script InstallGlow

# When it finish to install db just type :
mkt s reverse shell
# or
mkt search reverse shell

# Enjoy it
```

## Options

```bash
Usage:
    # Base install and uninstall tools.
    mkt   install     [<tools name>, <.mkt files>]
    mkt   uninstall    <tools name>
    mkt   reinstall    <tools name>
    mkt   upgrade      <tools name>
    mkt   upgrade      all

List:
    # List install the tools name.
    mkt   list     install
    mkt   list     installable

Script:
    # List build-in script
    mkt   script   list
    mkt   script   info
    # Run the script 
    mkt   script   <script_name>

DB and res:
    mkt   db   installable
    mkt   db   list
    mkt   db   install       <db_name>
    mkt   db   uninstall     <db_name>

Search DB and res:
    mkt   search   <string>

Other:
    # Update all the source include mkt.
    mkt-update

    # Remove all "__pycache__" in tools
    mkt clearup 
```

## Collection Tools List

```bash
$ sudo mkt list installable               
[*] Installable Tools List:
    Binary/Ghidra
    Tools/JSPWebShellCollection
    Tools/GrepForOSINT
    Tools/XC
    Tools/Htshells
    Tools/NmapAutomator
    Tools/ReverseSSH
    Tools/Tools4mane
    Tools/HackBrowserData
    Tools/EyeWitness
    Tools/Webshells_BlackArch
    Tools/Chisel
    Tools/Godzilla
    Windows/Gosecretsdump
    Windows/Boodhound
    Windows/Mimikatz
    Windows/Wesng
    Windows/KaliWinBinary
    Windows/WinPWN
    Windows/SharpCollection
    Windows/PrintSpoofer
    Windows/WinPEAS
    Windows/Powershell/Nishang
    Windows/Powershell/PSHTML
    Windows/Powershell/NetSPI
    Windows/Powershell/ADACLScanner
    Windows/Powershell/PrivescCheck
    Windows/Powershell/ADEssentials
    Windows/Powershell/ADPeas
    Windows/Powershell/AdsiPS
    Windows/Powershell/Sherlock
    Windows/Powershell/ADModule
    Windows/Powershell/PowerSploit_Master
    Windows/Powershell/VulnerableAD
    Windows/Powershell/BadBlood
    Windows/Powershell/RedTeamPowershellScripts
    Windows/Powershell/PowerShellSuite
    Windows/Powershell/RedTeamPowershellEnum
    Windows/Powershell/PowerSploit_Dev
    Windows/Powershell/Privesc
    Windows/Powershell/ADLab
    Windows/Powershell/PowerUpSQL
    Windows/Potato/RottenPotato
    Windows/Potato/RoguePotato
    Windows/Potato/Juicypotato
    Linux/Sudo_killer
    Linux/LinEnum
    Linux/LES2
    Linux/LinPEAS
    Linux/LES
    Linux/Pspy
    Wordlists/Rockyou
    Wordlists/SecLists
    Wordlists/AutoWordlists
    Wordlists/DOC
    Wordlists/Kkrypt0nn
```

## Collection DB

```bash
$ sudo mkt db installable     
[*] List all installable db ...
    XapaxSecurity
    Cheatsheet
    KaliDocs
    PWKCheatsheet
    IRedTeam
    LOLBAS
    GTFOBin
    PayloadsAllTheThings
    ADCheatsheet_drak3hft7
    PentestCheatSheets
    AtomicRedTeam
    PentestBook
    ADExploitation
    Ruuand
    ADCheatsheet_S1ckB0y1337
    HackTricks
    RedTeamWiki
    BaseDB
    Tools/Mimikatz
    Tools/BloodHound
```

## Later ...
