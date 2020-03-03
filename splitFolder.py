import os, os.path, sys
import shutil

filesPerFolder = 5000
fileCount = 0;
prefix_small_folder = 'splitted_'
for root, _, files in os.walk(sys.argv[1]):
    folderCount = len(files) / 5000
    for index in range(folderCount):
        try:
            os.makedirs(sys.argv[1] + '/' + prefix_small_folder + str(index))
        except Exception as e:
            print(str(e))
    for f in files:
        fileCount+=1
        fullpath = os.path.join(root, f)
        try:
            shutil.move(fullpath, sys.argv[1]+ '/' + prefix_small_folder+str(fileCount % folderCount))
        except Exception as e:
            print(str(e))
