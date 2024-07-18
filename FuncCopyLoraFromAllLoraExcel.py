import pandas as pd
import os
import shutil
ORIGIN_LORA_FIDR = "D:\\ComfyUI\\ComfyUI_windows_portable_nvidia_cu118_or_cpu\\ComfyUI_windows_portable\\ComfyUI\\models\\loras"

df = pd.read_excel("全Lora.xlsx", sheet_name="角色")
for index, content in df.iterrows():
    loraName = content["人物Lora列表"]
    originLoraPath = os.path.join(ORIGIN_LORA_FIDR, loraName)
    targetLoraPath = os.path.join(".//loras//", loraName)
    if not os.path.exists(targetLoraPath) and os.path.exists(originLoraPath):
        os.makedirs(os.path.dirname(targetLoraPath), exist_ok=True)  
        shutil.copy(originLoraPath, targetLoraPath)
        print(f"Copy {loraName} to {targetLoraPath}")
    
