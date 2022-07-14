import imp
import os
from os.path import join
import string
directory = "/home/marko/Desktop/studium/msc_computer_science/semester2/computer_vision/mariusordner/"

tackle = 'Annotations/480p/'

path = join(directory,tackle)
print(path)
all_directories = next(os.walk(path))[1]
count_empty = 0

for dir in all_directories:
    sub_dir = os.path.join(path, dir)
    print(dir)
    files = os.listdir(sub_dir)
    files.sort()
    i = 0
    for file in files:
        print(file)
        os.rename(join(sub_dir, file), join(sub_dir, file[:9]))
        #os.rename(join(sub_dir, file),join(sub_dir, str(i).zfill(5)+'.jpg'))
        i += 1
