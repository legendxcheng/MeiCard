"""
1. 判断图片长宽比，如果长大于宽较多（长/宽 > 1.3)，则放置到portrait文件夹
2. 如果宽大于长较多（宽/长 > 1.3)，则放置到landscape文件夹
3. 否则两者都放置

"""
import os
from PIL import Image

def resize_image_to_fit(image, target_width, target_height):
    original_width, original_height = image.size
    aspect_ratio = original_width / original_height

    # 计算新的尺寸
    if target_width / target_height > aspect_ratio:
        # 如果目标宽高比大于原始宽高比，以高度为基准进行缩放
        new_height = target_height
        new_width = int(new_height * aspect_ratio)
    else:
        # 以宽度为基准进行缩放
        new_width = target_width
        new_height = int(new_width / aspect_ratio)

    return image.resize((new_width, new_height), Image.ANTIALIAS)

def overlay_images(background_path, overlay_image, output_path, placement='center'):
    """
    将覆盖图片放置到背景图片上，支持中心放置和黄金分割放置。
    
    :param background_path: 背景图片路径
    :param overlay_image: PIL Image对象，覆盖图片
    :param output_path: 输出图片路径
    :param placement: 放置方式，'center' 或 'golden_ratio'
    """
    # 打开背景图像
    background = background_path.convert('RGBA')

    # 获取背景图像的尺寸
    bg_width, bg_height = background.size

    # 调整覆盖图像的尺寸
    overlay = resize_image_to_fit(overlay_image, bg_width, bg_height).convert('RGBA')

    # 获取调整后覆盖图像的尺寸
    overlay_width, overlay_height = overlay.size

    # 根据放置方式计算放置位置
    if placement == 'center':
        x = (bg_width - overlay_width) // 2
        y = bg_height - overlay_height  # 贴着下边缘
    elif placement == 'golden_ratio':
        golden_ratio = 1.618
        x = int((bg_width - overlay_width) / golden_ratio)
        y = bg_height - overlay_height  # 贴着下边缘
    else:
        raise ValueError("Invalid placement option. Use 'center' or 'golden_ratio'.")

    # 创建一个新的图像，将背景和覆盖图像合并
    combined = Image.alpha_composite(background, Image.new('RGBA', background.size))
    combined.paste(overlay, (x, y), overlay)

    # 保存最终的图像
    combined.save(output_path, 'PNG')
    print(f"Saved overlaid image to {output_path}")





if __name__ == "__main__":
    # 遍历文件夹中的所有文件
    folderPath =  "D:\\魅卡\\骨骼图\\RawGrow\\"
    os.makedirs("D:\\魅卡\\骨骼图\\landscape", exist_ok=True)
    os.makedirs("D:\\魅卡\\骨骼图\\portrait", exist_ok=True)

    landscapeBackground = Image.open("landscapeBase.png")
    portraitBackground = Image.open("portraitBase.png")

    for root, _, files in os.walk(folderPath):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image = Image.open(os.path.join(root, filename))
                iw, ih = image.width, image.height

                if iw / ih > 1.2: # landscape
                    overlay_images(landscapeBackground, image, os.path.join("D:\\魅卡\\骨骼图\\landscape", filename))
                    pass
                elif ih / iw > 1.2: # portrait
                    overlay_images(portraitBackground, image, os.path.join("D:\\魅卡\\骨骼图\\portrait", filename))
                    pass
                else: #both
                    overlay_images(landscapeBackground, image, os.path.join("D:\\魅卡\\骨骼图\\landscape", filename), placement='golden_ratio')
                    overlay_images(portraitBackground, image, os.path.join("D:\\魅卡\\骨骼图\\portrait", filename), placement='golden_ratio')
                    pass
