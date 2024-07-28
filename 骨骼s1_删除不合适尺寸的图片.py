import os
from PIL import Image

def delete_non_image_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not (file.lower().endswith('.png') or file.lower().endswith('.jpg') or file.lower().endswith('.jpeg')):
                try:
                    os.remove(os.path.join(root, file))
                    print(f"Deleted non-image file: {os.path.join(root, file)}")
                except Exception as e:
                    print(f"Error deleting file {os.path.join(root, file)}: {e}")

def delete_images_with_invalid_aspect_ratio(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png') or file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
                file_path = os.path.join(root, file)
                try:
                    with Image.open(file_path) as img:
                        width, height = img.size
                        aspect_ratio = width / height
                        if aspect_ratio < 0.5 or aspect_ratio > 2.0:
                            img.close()  # Ensure the file is closed before attempting to delete
                            os.remove(file_path)
                            print(f"Deleted image with invalid aspect ratio: {file_path}")
                except Exception as e:
                    print(f"Error processing file {file_path}: {e}")

def clean_directory(directory):
    delete_non_image_files(directory)
    delete_images_with_invalid_aspect_ratio(directory)

if __name__ == "__main__":
    directory = "D:\\魅卡\\骨骼图\\F0025\\日式手办图片集24000P\\"  # Replace with the path to your directory
    clean_directory(directory)
