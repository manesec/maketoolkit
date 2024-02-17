# maketoolkit

Quick to install some pen-testing tools on python env and debian like os.

![Logo](Picture/main.png)

Some of the tools are integrated by [@manesec](https://github.com/manesec).

This tool has part of the script to make it easier for you to use it without the need for frequent download tools, just like the apt package manager.

# Warning

This is **BETA** version, which mean it need to very unstable, also still updating. If you find a bug just feel free to submit the issue, you may need to update before to use.

If you upgrade `mkt` all the tools in `/Tools` will be delete, you can re-install it later.

Some tools maybe not working on your system due to system environment, I am trying to fix it.

Some script may broken your system, **Please do not install on your host machine.**

Recommend use it on **kali** system.

## Quick Start

To install `mkt` command just: 

```bash
git clone https://github.com/manesec/maketoolkit.git
cd maketoolkit; chmod u+x *.sh; sudo python3 install.py
```

**Note**: All tools will be locate in `/var/lib/mkt/Tools/Source` which soft link to `/Tools`.

## Structure

There are 5 main structure, `Tools` , `Search DB` and `Script` ,

+ `Tools` is use to install the pen-test tools.

+ `Search DB` is use to search local document. It mean you need to download search db before to use.

+ `Script` is some script, use to install some tools or setup the env.

+ `Docker` is use to help for automatic build custom docker image.

+ `Venv` is use to help for automatic build python virtual environment.

A Config file will be locate in `/etc/mkt.conf`.

## About Tools

If you finish to install `mkt`, just goto `/Tools` to look around that.

all tools will be end with `.mkt`, you can list with `mkt list installable` command.

```bash
~ $ mkt list installable
[*] Installable Tools List:
    Binary/CarbonCopy
    Binary/Ghidra

~ $ ls /Tools
Binary  Linux  Tools  Windows  Wordlists

~ $ cd /Tools/Linux
ContainerEscapeCheck.mkt  DDexec.mkt  Deepce.mkt  LES.mkt  LES2.mkt  LinEnum.mkt  LinPEAS.mkt  Pspy.mkt  Sudo_killer.mkt
```

To install a tools, just type `sudo mkt install <path_to_mkt>` or `sudo mkt install <name>`.

```bash
~ $ sudo mkt install LinPEAS     
[LinPEAS] Downloading base ...
 *  Searching Github Repo ...
 +  Found linpeas.sh 

# or
~ $ sudo mkt install linpeas
~ $ sudo mkt install LinPEAS.mkt
~ $ sudo mkt install /Tools/Linux/LinPEAS.mkt
```


## About Search DB

If you want to install an offline documents, just use those command to install it.

```bash
~ $ mkt db installable   
[*] List all installable db ...
    BaseDB
    HackTricks
    PayloadsAllTheThings

# Install search db.
sudo mkt db install BaseDB
sudo mkt db install HackTricks
sudo mkt db install PayloadsAllTheThings
```

If you want to use build-in local web server, just type `mkt doc` to start the server.


## About Script

Some script may help you, If you need to run just type `sudo mkt script <number>`.

```bash
~ $ mkt script list              
There are available scripts: 
--------------------------------------------------
[0] Install/AllSearchDB
[1] Install/BasicTools
[2] Install/Glow
[3] Install/GoSpider
[4] Install/NTH
[5] Install/OnlyOffice
[6] Install/Raccon
[7] Install/Xortool
[8] Run/SetupNeo4j

# Run Setup Neo4j without password
~ $ sudo mkt script 8 

# More information
~ $ mkt script info  
```

## Advanced Settings: Search DB

Search DB now support grep, ripgrep, whoosh to search the document.

```bash
# using ripgrep search engine
sudo apt install ripgrep

# using whoosh search engine
sudo pip3 install whoosh
sudo mkt db reindex # only whoosh need to index
```

You can choose what search engine you need, change on config file:

```bash
# Define what search engine you want to use.
# Available: grep, ripgrep, whoosh
SearchEngine = grep
```

Default is using `grep` to search, it's slow.

### Example to using whoosh search engine:

You can change it to using whoosh engine to speed up your search.

Before to using whoosh just type:

```bash
sudo pip3 install whoosh
```

and change the config `/etc/mkt.conf` like :

```bash
SearchEngine = whoosh
```

finally, update the index.

```bash
sudo mkt db reindex
```

## Update

Just type `sudo mkt-update` to update the tools, **but all tools will be delete it Because it need to reinstall the source**, which mean you need to install the tools again.

## More Example for the command

```bash
# ========== Install some Tools ==========
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
sudo mkt script info

# use the script
sudo mkt script <script_name> 
sudo mkt script <script_index>

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
    mkt      install          [<tools name>, <.mkt files>]
    mkt   uninstall/remove    <tools name>
    mkt      reinstall        <tools name>
    mkt      upgrade          <tools name>
    
    # Uhm, No Recommand.
    mkt      upgrade          all

List:
    # List install the tools name.
    mkt      list             install
    mkt      list             installable

Script:
    # List build-in script
    mkt      script           list
    mkt      script           info
    mkt      script           help

    # Run the script 
    mkt      script           <script_name>
    mkt      script           <script_index>

Virtual Env:
    mkt      docker    list
    mkt      docker    run       <name>    <option>
    mkt      docker    build     <name>
    mkt      docker    rebuild   <name>
    mkt      venv      list
    mkt      venv      run       <name>
    mkt      venv      remove    <name>
    mkt      venv      rebuild   <name>

DB and res:
    mkt        db         installable
    mkt        db         install       <db_name>
    mkt        db         uninstall     <db_name>
    mkt        db         upgrade       <db_name> / all
    mkt        db         reindex

Search DB and find in file:
    mkt     s(earch)          <string>
    mkt     f(ind)            <string>

Other:
    # Update the mkt core, will delete all the tools, 
    # You need to reinstall all the tools ;(
    sudo mkt-update
```
Hope you love this.

## Please give me some time to update ...
## Still Updating ...