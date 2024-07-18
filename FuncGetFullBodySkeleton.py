#009933
#009966
#009900
#009999
#006699
#003399
#999900
#996600
#339900
#669900
#993300
#990000
#000099
#990099
#990066
#330099
#660099

import os
from PIL import Image
import shutil

# 定义文件夹路径
folder_A = 'D:\\魅卡\\骨骼图\\landscape'
folder_B = 'D:\\魅卡\\骨骼图\\landscape全身'

# 定义需要检查的颜色列表
required_colors = [
    '#009933', '#009966', '#009900', '#009999', '#006699', '#003399',
    '#999900', '#996600', '#339900', '#669900', '#993300', '#990000',
    '#000099', '#990099', '#990066', '#330099', '#660099'
]

# 将颜色从十六进制转换为RGB元组
required_colors_rgb = [tuple(int(color[i:i+2], 16) for i in (1, 3, 5)) for color in required_colors]

# 遍历文件夹A中的所有PNG文件
for filename in os.listdir(folder_A):
    if filename.lower().endswith('.png'):
        file_path = os.path.join(folder_A, filename)
        
        # 打开图像并获取像素数据
        with Image.open(file_path) as img:
            img = img.convert('RGB')  # 确保图像为RGB模式
            pixels = list(img.getdata())
        
        # 检查图像是否包含所有指定颜色
        if all(color in pixels for color in required_colors_rgb):
            # 如果包含所有指定颜色，则将文件复制到文件夹B
            shutil.copy(file_path, folder_B)
            print(f"Copied {filename} to {folder_B}")

print("Processing completed.")
