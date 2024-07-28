import os
import hashlib
from PIL import Image

def calculate_image_hash(image_path):
    """计算图片的哈希值"""
    with Image.open(image_path) as img:
        # 将图片转换为RGB模式并调整大小
        img = img.convert('RGB')
        img = img.resize((8, 8), Image.ANTIALIAS)
        # 计算哈希值
        hash_value = hashlib.md5(img.tobytes()).hexdigest()
    return hash_value

def find_and_remove_duplicates(folder_path):
    """查找并删除重复的图片"""
    # 存储图片哈希值和路径的字典
    hash_dict = {}
    # 遍历文件夹中的所有文件
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(root, filename)
                try:
                    # 计算图片的哈希值
                    image_hash = calculate_image_hash(file_path)
                    if image_hash in hash_dict:
                        # 如果哈希值已经存在，删除当前图片
                        os.remove(file_path)
                        print(f"Removed duplicate image: {file_path}")
                    else:
                        # 否则，存储哈希值和路径
                        hash_dict[image_hash] = file_path
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

# 设置图片文件夹路径
folder_path = 'D:\\魅卡\\骨骼图\\RawCrop\\'

# 调用函数查找并删除重复的图片
find_and_remove_duplicates(folder_path)
