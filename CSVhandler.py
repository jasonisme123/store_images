import csv
import os


def init_csv():
    # 定义列名
    fieldnames = ['desc', 'filename']
    with open('images_record.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()  # 写入列名


def add_csv(row):
    current_path = os.getcwd()  # 获取当前路径
    file_path = os.path.join(current_path, 'images_record.csv')
    if not os.path.exists(file_path):
        init_csv()
    # 追加数据到CSV文件
    with open('images_record.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)  # 写入数据


def get_image_from_index(data_index):
    with open('images_record.csv') as f:
        reader = csv.reader(f)
        # 获取第n行的数据
        line = next(reader)   # 获取第一行
        for i in range(data_index+1):
            line = next(reader)
        return line[1]


def get_csv():
    # 打开 CSV 文件
    texts = []
    with open('images_record.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        for i, line in enumerate(reader):
            if i != 0:
                texts.append(line[0])

    return texts
