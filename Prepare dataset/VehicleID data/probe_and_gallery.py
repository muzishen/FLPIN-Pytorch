import os
import shutil
import random
#只要更改路径即可

#随机读取函数
def random_read(gallery_save_path, query_save_path):
    gallery_path = os.listdir(gallery_save_path) #gallery 类别路径
    for i in gallery_path:
        query_path = query_save_path + '/' + i # 查询库类别路径
        if not os.path.exists(query_path): #如果查询类别路径不存在，则创建
            os.mkdir(query_path)
        src_path = gallery_save_path + '/' + i
        test_img = os.listdir(src_path) #读取每个类别里面的文件列表
        img_num = random.sample(test_img, 1) #随机取一个文件
        src_path = src_path + '/' + img_num[0]
        dst_path = query_path + '/' + img_num[0]
        shutil.move(src_path, dst_path) #移动文件


#=============test800,之后根据修改number
download_path = r'I:/xieyi/VehicleID_V1.0'
train_path = download_path + '/train_test_split/test_list_800.txt' #读取txt文件 下面800一样需要修改

f = open (train_path, 'r')
lines = f.readlines()

for j in range(10):
#创建test，并按照图像ID进行分别存放，文件名为 id_number
    os.mkdir(download_path + '/data_800_'+ str(j))
    gallery_save_path = download_path + '/data_800_'+ str(j) + '/probe_800_' + str(j)
    query_save_path = download_path + '/data_800_'+ str(j) + '/gallery_800_' + str(j)
    if not os.path.isdir(gallery_save_path):
        os.makedirs(gallery_save_path)
        os.makedirs(query_save_path)
    for line in lines:
        line_array = line.split()
        img_number = line_array[0]   #图片原名
        img_class = line_array[1]   #图片类别
        test_src_name = 'I:/xieyi/VehicleID_V1.0/image/' + img_number + '.jpg'#源文件
        test_dst_path = gallery_save_path + '/' + img_class  #创建类别文件夹
        print(test_dst_path)
        if not os.path.exists(test_dst_path):
            os.makedirs(test_dst_path)
        test_dst_name = test_dst_path + '/' + img_class + '_' + img_number + '.jpg'#源文件存放位置并且重命名为id_number
        print(test_dst_name)
        if os.path.exists(test_src_name):
            shutil.copy(test_src_name, test_dst_name)
    #----
    #随机读取创建query
    random_read(gallery_save_path, query_save_path)
