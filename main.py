import Images_handler
import find_similar


def load_images():
    # 把需要加入的图片放入temp_images目录下
    Images_handler.main()


def find_images(desc):
    # 返回图片列表
    res = find_similar.main(desc)
    print(res)


if __name__ == '__main__':
    # load_images()
    find_images('化妆品')
