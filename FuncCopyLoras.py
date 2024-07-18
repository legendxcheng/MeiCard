# 读取指定的JSON文件，找到所有CR LoRA Stack的结点，找到所有Lora的结点路径，去重汇总
# 将去重后的文件，以相同的路径复制到指定目录下

IMAGE_DIR = "D:\\魅卡\\热辣滚滚第二弹\\"
ORIGIN_LORA_FIDR = "D:\\ComfyUI\\ComfyUI_windows_portable_nvidia_cu118_or_cpu\\ComfyUI_windows_portable\\ComfyUI\\models\\loras"

import os
from PIL import Image
import json
import shutil

global loraPaths
loraPaths = []

def read_meta_info(file_path):
    global loraPaths
    try:
        with Image.open(file_path) as img:
            prompt = json.loads(img.info['prompt'])
            for nodeKey in prompt:
                node = prompt[nodeKey]
                if node['class_type'] == 'CR LoRA Stack':
                    print(f"Found CR LoRA Stack node: {nodeKey}")
                    for inputKey in node['inputs']:
                        if inputKey.startswith('lora_name_'):
                            loraPath = node['inputs'][inputKey]
                            if loraPath != "None":
                                loraPaths.append(loraPath)
    except Exception as e:
        pass
        # print(f"Error reading {file_path}: {e}")

def recursive_traverse(directory):
    global loraPaths
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                file_path = os.path.join(root, file)
                read_meta_info(file_path)
    loraPaths = list(set(loraPaths))
    pass

if __name__ == "__main__":
    
    directory_A = IMAGE_DIR  # 替换为实际的目录路径
    recursive_traverse(directory_A)

    for lp in loraPaths:
        originFullPath = os.path.join(ORIGIN_LORA_FIDR, lp)
        targetFullPath = os.path.join(".//loras//",  lp)
        if not os.path.exists(targetFullPath):
            os.makedirs(os.path.dirname(targetFullPath), exist_ok=True)  
            shutil.copy(originFullPath, targetFullPath)
            print(f"Copy {lp} to {targetFullPath}")
        else:
            print(f"skipo {lp}")


