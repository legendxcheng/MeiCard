import pandas as pd
import os
import shutil
import time

ORIGIN_LORA_FIDR = "D:\\ComfyUI\\ComfyUI_windows_portable_nvidia_cu118_or_cpu\\ComfyUI_windows_portable\\ComfyUI\\models\\loras"

# 读取Excel文件
df = pd.read_excel("全Lora.xlsx", sheet_name="角色")

# 获取当前时间的时间戳
current_time = time.time()

for index, content in df.iterrows():
    loraName = content["人物Lora列表"]
    if content['人气角色'] != 1:
        continue
    
    originLoraPath = os.path.join(ORIGIN_LORA_FIDR, loraName)
    targetLoraPath = os.path.join(".//loras//", loraName)
    
    # 检查文件是否存在
    if os.path.exists(originLoraPath):
        # 获取文件的创建时间
        creation_time = os.path.getctime(originLoraPath)
        
        # 检查文件创建时间是否在24小时内
        if current_time - creation_time <= 72 * 60 * 60:
            if not os.path.exists(targetLoraPath):
                os.makedirs(os.path.dirname(targetLoraPath), exist_ok=True)
                shutil.copy(originLoraPath, targetLoraPath)
                print(f"Copy {loraName} to {targetLoraPath}")
