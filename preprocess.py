from PIL import Image
import os
from os.path import join
import shutil
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--anno_folder', required=True)
parser.add_argument('-c', '--max_col', required=False, default=5)
args = parser.parse_args()

annotations_dict = args.anno_folder

MAX_COLORS= args.max_col

# get n most common colours in an image

def getMostCommonColours(n: int, img: np.array):
  col_array = img.reshape(-1)
  unique, counts = np.unique(col_array, axis=0, return_counts=True)
  zipped = list(zip(unique, counts))
  zipped.sort(key=lambda tup: tup[1],reverse=True)
  return [i[0] for i in zipped[:n]]
  
def keepNColorsAndBlackOutTheRest(n: int, img):
  np_img = np.array(img)
  colors = getMostCommonColours(n, np_img)
  img_as_list = np_img.tolist()
  print(colors)
  img_as_list_reduced_col = [
                             [
                              0
                              if col not in colors
                              else col
                              for col in row
                              ]
                             for row in img_as_list
                             ]

  new_img = np.array(img_as_list_reduced_col)
  return Image.fromarray(new_img.astype('uint8'))

# delete everyting in Annotations exept folder 4

all_directories = next(os.walk(annotations_dict))[1]
count_empty = 0

for dir in all_directories:
    sub_dir = os.path.join(annotations_dict, dir)
    files = os.listdir(sub_dir)
    for element in files:
        if element != '4' and not element.endswith("png"):
            try:
                os.remove(os.path.join(sub_dir, element))
            except:
                shutil.rmtree(os.path.join(sub_dir, element))


# extract images out of folder 4
for dir in all_directories:
    sub_dir = os.path.join(annotations_dict, dir)
    try:
        files = os.listdir(os.path.join(sub_dir, str(4)))
        for element in files:
            shutil.move(os.path.join(sub_dir, str(4), element), os.path.join(sub_dir, element))
        os.rmdir(os.path.join(sub_dir, str(4)))
    except:
        pass

# rename 

for dir in all_directories:
    sub_dir = os.path.join(annotations_dict, dir)
    files = os.listdir(sub_dir)
    files.sort()
    i = 0
    for file in files:
        os.rename(join(sub_dir, file),join(sub_dir, str(i).zfill(5)+'.png'))
        i += 1


# max_color annotations



for dir in all_directories:
    sub_dir = os.path.join(annotations_dict, dir)
    print(dir)
    files = os.listdir(sub_dir)
    for file in files:
        img = Image.open(join(sub_dir, file))

        # Merge similar colours
        reduced_img =  img.convert('P', palette=Image.ADAPTIVE, colors=MAX_COLORS)
        reduced_img.save(join(sub_dir, file), 'PNG')

# scale 

for dir in all_directories:
    sub_dir = os.path.join(annotations_dict, dir)
    print(dir)
    files = os.listdir(sub_dir)
    for file in files:
        im = Image.open(join(sub_dir, file))
        imResize = im.resize((1152, 480), Image.NEAREST)
        imResize.save(join(sub_dir, file) + ' resized.png', 'PNG', quality=90)

for dir in all_directories:
    sub_dir = os.path.join(annotations_dict, dir)
    print(dir)
    files = os.listdir(sub_dir)
    for file in files:
        if not file.endswith('resized.png'):
            print(file)
            os.remove(join(sub_dir, file))


# remove resized.png tail

for dir in all_directories:
    sub_dir = os.path.join(annotations_dict, dir)
    print(dir)
    files = os.listdir(sub_dir)
    files.sort()
    i = 0
    for file in files:
        print(file)
        os.rename(join(sub_dir, file), join(sub_dir, file[:9]))
        i += 1