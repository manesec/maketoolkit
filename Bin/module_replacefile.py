import shutil,os

def replaceLineFromfile(file_path, text, replace_text):
    tmp_save = open( "/tmp/mkt.replace" , 'w', encoding='utf-8')
    with open(file_path,'r',encoding='utf-8') as readfile:
        for line in readfile:
            if text in line:
                tmp_save.writelines(replace_text + "\n")
                print("Patched !")
                continue
            tmp_save.writelines(line)
        readfile.close()
    tmp_save.close()
    os.remove(file_path)
    shutil.move('/tmp/mkt.replace',file_path)