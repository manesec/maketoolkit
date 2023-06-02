def Info():
    print("Install gospider from https://github.com/jaeles-project/gospider.git")

def Run():
    import os
    os.system("GO111MODULE=on go install github.com/jaeles-project/gospider@latest")
    os.system("cp ~/go/bin/gospider /bin/gospider")
    print("Install done. Example:")
    print("    $ gospider -s <webside>  --js --sitemap --robots --subs -d 10 -w")