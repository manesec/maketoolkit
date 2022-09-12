# maketoolkit

Quick to install some pen-testing tools on python and debian like os.

![Logo](Picture/main.png)

# Warning

This is **BETA** version, which mean it need to very unstable, also still updating. If you find a bug just feel free to submit the issue, you may need to update before to use.

## Base Installation

This command only install `mkt` command, not any search db or tools, but you can install it manualy by using `mkt db install` or `mkt install` command.

```bash
git clone https://github.com/manesec/maketoolkit.git
cd maketoolkit; chmod u+x *.sh; sudo ./install.sh
```

**Note**: All tools will be locate in `/var/lib/mkt/Tools/Source` which soft link to `/Tools`.

You can setup it on `kali` or `parrot os` in those command.

```bash
cd ~
rm -rf ~/maketoolkit
git clone https://github.com/manesec/maketoolkit.git
cd maketoolkit ; chmod u+x *.sh; sudo ./reinstall.sh
# Install some tools.
sudo mkt script InstallBasicTools
# Install search db.
sudo mkt db install BaseDB
sudo mkt db install HackTricks
sudo mkt db install TheHackerRecipes
sudo mkt db install Priv2Admin
sudo mkt db install PayloadsAllTheThings
```

Just copy and paste in your terminal, after finished, just type `mkt` command to verify if it install seccessful.

## Structure

There are 3 main structure, `Tools` , `Search DB` and `Script` ,

+ `Tools` is use to install the pen-test tools.

+ `Search DB` is use to search local document. It mean you need to download search db before to use.

+ `Script` is some script, use to install some tools or setup the env.

## Update

Just type `sudo mkt-update` to update the tools, **but all tools will be delete it Because it need to reinstall the source**, which mean you need to install the tools again.

## Tutorial about the command.

```bash
# ========== Tools ==========
# If you need to see what tools can be install: 
sudo mkt list installable

# Install the tools, just type tools name: 
sudo mkt install Windows/WinPEAS

# Or, goto /Tools/Linux and :
sudo mkt install LinPEAS.mkt

# ========== Search DB ==========
# What db can be installable: 
sudo mkt db installable

# (Recommend) If you want to support to view .md file, you need to:
sudo mkt script InstallGlow

# Before you need to search, you need to install search db.
sudo mkt db install HackTricks

# When it finish to install db just type :
mkt s reverse shell
# or
mkt search reverse shell

# ========== Script ==========
# List all the script
sudo mkt script list

# use the script
sudo mkt script <script_name> 

# ========== Other ==========
# Update mkt tools and the source just type:
# All the tools will be delete.
sudo mkt-update

# Enjoy it
```

## Usage

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
Hope you love this.

## Still Updating ...