import os
import shutil

from_dir="c:/Users/admin/Downloads"
to_dir="./organised_files"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    #print(name)
    #print(extention)
    #print(file_name)
    
    if extention=="":
        continue
    
    if extention in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+extention
        path3=to_dir+"/"+extention+"/"+file_name
        
        #print(path1)
        #print(path3)
        
        if os.path.exists(path2):
            print("moving"+file_name+"...")
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("moving"+file_name+"...")
            shutil.move(path1,path3)
            