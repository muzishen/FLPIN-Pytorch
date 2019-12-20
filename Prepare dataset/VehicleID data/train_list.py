import os
import shutil
import random
#只要更改路径即可


#=============test800,之后根据修改number
download_path = r'I:/xieyi/VehicleID_V1.0' # 数据集路径
train_path = download_path + '/train_test_split/train_list.txt' #读取txt
train_image_path = download_path + '/train_image'

f = open (train_path, 'r')
lines = f.readlines()


if not os.path.exists(train_image_path):
    os.mkdir(train_image_path)


for image_every in lines:
    image_name = image_every.split(" ")[0]
    image_id = image_every.split(" ")[1].strip('\n')
    train_image_id_path = train_image_path + '/' + image_id
    if not os.path.exists(train_image_id_path):
        os.mkdir(train_image_id_path)

    src_path = download_path + '/image/' + image_name + '.jpg'
    dst_path = train_image_id_path + '/' + image_id + '_' + image_name + '.jpg'
    shutil.copyfile(src_path, dst_path)


