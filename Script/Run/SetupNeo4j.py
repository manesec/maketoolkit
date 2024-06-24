def Info():
    print("""This script will be setup Setup neo4j and run neo4j: 
    - neo4j: no password""")

def Run():
    from importlib.machinery import SourceFileLoader
    SourceFileLoader("require_root","/var/lib/mkt/Bin/module_unit.py").load_module().RequireRoot()

    import os,sys

    if (os.path.exists("/etc/neo4j/neo4j.conf") == False):
        print("[!] No found config files on /etc/neo4j/neo4j.conf")
        sys.exit(0)

    print("[*] Reading config ...")
    write_file = open("/etc/neo4j/neo4j.conf.new","w")
    with open("/etc/neo4j/neo4j.conf","r") as read_file :
        for line in read_file:
            if (line.find("#dbms.security.auth_enabled=false") !=-1):
                line = line.replace("#dbms.security.auth_enabled=false","dbms.security.auth_enabled=false")
            write_file.writelines(line)
    write_file.close()

    os.system("cp /etc/neo4j/neo4j.conf.new /etc/neo4j/neo4j.conf")

    print("[*] Running neo4j ...")
    os.system("neo4j console")