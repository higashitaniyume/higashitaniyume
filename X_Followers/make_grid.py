#
# 此代码是用来把fo们的头像拼起来成一个超大的图片的python脚本。
# 你可以随意使用这里面的代码，可以不经过我的许可，也不需要署名或者保留这个注释，这个代码是自由使用的~
#
import os
import time
from PIL import Image


def make_grid_from_latest(rows, cols, base_folder="."):
    latest_folder = base_folder
    print(f"使用文件夹: {latest_folder}")
    
    img_files = [os.path.join(latest_folder, f) for f in os.listdir(latest_folder) 
                 if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    img_files.sort()
    
    total = len(img_files)
    if rows * cols < total:
        img_files = img_files[:rows * cols]
    
    sample = Image.open(img_files[0])
    w, h = sample.size
    
    grid_img = Image.new("RGB", (cols * w, rows * h), color=(255, 255, 255))
    
    for idx, file in enumerate(img_files):
        img = Image.open(file).resize((w, h))
        row = idx // cols
        col = idx % cols
        grid_img.paste(img, (col * w, row * h))
    
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_file = f"./output/grid_{timestamp}.jpg"
    grid_img.save(output_file)
    print(f"拼图完成，保存为 {output_file}")

if __name__ == "__main__":
    make_grid_from_latest(rows=11, cols=11, base_folder="./2025")
