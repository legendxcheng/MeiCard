from PIL import Image
import os

def crop_black_background(image_path, output_path):
    # 打开图像
    image = Image.open(image_path)
    image = image.convert('RGB')  # 确保图像是RGB模式

    # 获取图像的宽度和高度
    width, height = image.size

    # 获取图像的像素数据
    pixels = image.load()

    # 初始化边界值
    left = width
    right = 0
    top = height
    bottom = 0

    # 遍历所有像素点，找到非黑色像素的最小边界
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            if r != 0 or g != 0 or b != 0:  # 非黑色像素
                if x < left:
                    left = x
                if x > right:
                    right = x
                if y < top:
                    top = y
                if y > bottom:
                    bottom = y

    # 裁剪图像
    if left < right and top < bottom:
        cropped_image = image.crop((left, top, right + 1, bottom + 1))
        cropped_image.save(output_path)
        print(f"Cropped image saved to {output_path}")
    else:
        print(f"No non-black pixels found in {image_path}")

def process_images(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename)
            crop_black_background(input_path, output_path)

# 设置输入和输出目录
input_directory = 'D:\\魅卡\\骨骼图\\portrait'
output_directory = 'D:\\魅卡\\骨骼图\\RawCrop'
os.makedirs(output_directory, exist_ok=True)

# 处理图像
process_images(input_directory, output_directory)
