#using os module we can list the directories and we can search for the files having extension as .TXT or .txt or .Txt etc


#instead of /mydir use the directory's path which u want to seach .txt extension files in 


import os
for file in os.listdir("/mydir"):
    if file.lower().endswith(".txt"):
        print(os.path.join("/mydir", file))

#WE CAN ALSO USE GLOB MODULE for the same  
"""import glob, os
os.chdir("/mydir")
for file in glob.glob("*.txt"):
    print(file)"""   