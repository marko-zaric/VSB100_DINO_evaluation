from PIL import Image
import os, sys
import imp
from os.path import join
import string
directory = "/home/marko/Desktop/studium/msc_computer_science/semester2/computer_vision/mariusordner/"

tackle = 'JPEGImages/480p/'

path = join(directory,tackle)
print(path)
all_directories = next(os.walk(path))[1]
count_empty = 0

for dir in all_directories:
    sub_dir = os.path.join(path, dir)
    print(dir)
    files = os.listdir(sub_dir)
    for file in files:
        im = Image.open(join(sub_dir, file))
        imResize = im.resize((1152, 480), Image.NEAREST)
        imResize.save(join(sub_dir, file) + ' resized.jpg', 'JPEG', quality=90)

for dir in all_directories:
    sub_dir = os.path.join(path, dir)
    print(dir)
    files = os.listdir(sub_dir)
    for file in files:
        if not file.endswith('resized.jpg'):
            print(file)
            os.remove(join(sub_dir, file))
