from PIL import Image
import os

def process_image(image_path, output_path):
    with Image.open(image_path) as img:
        width, height = img.size
        new_width = int(width * 1.2)  # 7.5% on both left and right
        new_height = int(height * 1.17)  # 10% on the top

        # Create a new image with black background
        new_img = Image.new('RGB', (new_width, new_height), (0, 0, 0))

        # Paste the original image onto the new image
        offset_x = int((new_width - width) / 2)
        offset_y = int(new_height - height)
        new_img.paste(img, (offset_x, offset_y))

        # Save the new image
        new_img.save(output_path)

def process_folder(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            output_path = os.path.join(output_folder, filename)
            process_image(image_path, output_path)

# Example usage
input_folder = 'D:\\魅卡\\骨骼图\\RawCrop'
output_folder = 'D:\\魅卡\\骨骼图\\RawGrow'
os.makedirs(output_folder, exist_ok=True)
process_folder(input_folder, output_folder)
