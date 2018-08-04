
import os
import shutil


src="<source_path>"
dest="<dest_path>"


files=os.listdir(src)


for file in files:
	fullpath=os.path.join(src,file)
	if(os.isfile(fullpath)):
          shutil.copy(fullpath,dest)

          
