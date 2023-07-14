import os
import re
from Images_desc import *
from CSVhandler import *
import shutil


def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


def get_images_files(filedir):
    current_path = os.getcwd()  # 获取当前路径
    folder_path = os.path.join(current_path, filedir)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    """递归获取指定文件夹下的所有文件"""
    files = []
    # 遍历文件夹下的所有文件和文件夹
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        # 判断是否是文件，如果是文件则添加到列表中
        if os.path.isfile(item_path):
            files.append(item_path)
        # 如果是文件夹，则递归获取该文件夹下的所有文件
        elif os.path.isdir(item_path):
            files.extend(list_all_files(item_path))

    sorted_files = sorted(
        files, key=lambda x: natural_sort_key(os.path.basename(x)))
    return sorted_files


def move_image_file(image_path, prefix_image, ext):
    current_path = os.getcwd()  # 获取当前路径
    dst_dir = os.path.join(current_path, 'final_images')
    new_filename = str(prefix_image)+ext
    # 构造新路径
    new_path = os.path.join(dst_dir, new_filename)
    shutil.move(image_path, new_path)


def main():
    # 要加入的图片放在temp_images目录下
    # 读取temp_images的图片，获得desc，加入csv，再把图片移动到final_images(修改文件名以确保文件名不重复)
    images_files = get_images_files('temp_images')
    len_final_images_files = len(get_images_files('final_images'))
    count = 0
    for image_file in images_files:
        count = count + 1
        desc = get_desc(image_file)
        filename = os.path.basename(image_file)
        ext = os.path.splitext(filename)[1]
        move_image_file(image_file, len_final_images_files+count, ext)
        cur_image_name = str(len_final_images_files+count)+ext
        add_csv([desc, cur_image_name])


# if __name__ == '__main__':
#     main()
