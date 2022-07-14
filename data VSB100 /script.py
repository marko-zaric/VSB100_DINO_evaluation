import imp
import os
from os.path import join
directory = "/home/marko/Desktop/studium/msc_computer_science/semester2/computer_vision/mariusordner/"

tackle = 'JPEGImages/480p/'

all_directories = next(os.walk(join(directory,tackle)))[1]
count_empty = 0
vids = []
for dir in all_directories:
    sub_dir = os.path.join(directory, dir)
    # files = os.listdir(sub_dir)
    print(dir)
    vids.append(dir)

with open('/home/marko/Desktop/studium/msc_computer_science/semester2/computer_vision/mariusordner/val.txt', 'w') as f:
    for line in vids:
        f.writelines(line)
        f.writelines('\n')
