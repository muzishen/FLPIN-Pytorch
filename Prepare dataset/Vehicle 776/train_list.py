import os
import shutil
import random
#只要更改路径即可


#=============test800,之后根据修改number
download_path = r'I:/All_data_tmp/VeRi776/VeRi'
train_path = download_path + '/name_train.txt'
train_image_path = 'E:/xieyi/EMDD_datasets/VeRi-776/train'

f = open (train_path, 'r')
lines = f.readlines()

if not os.path.exists(train_image_path):
    os.mkdir(train_image_path)

train_image_path = train_image_path + '/class_id'
if not os.path.exists(train_image_path):
    os.mkdir(train_image_path)

for image_name in lines:

    image_name = image_name.strip("\n")
    image_name_split  = image_name.split("_")
    image_class = image_name_split[0]
    print(image_class)
    train_image_class_path = train_image_path + '/' + image_class
    if not os.path.exists(train_image_class_path):
        os.mkdir(train_image_class_path)

    src_path = download_path + '/image_train/' + image_name
    dst_path =  train_image_class_path + '/' + image_name
    shutil.copyfile(src_path, dst_path)


