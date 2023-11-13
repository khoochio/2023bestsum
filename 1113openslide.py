import tarfile
file_name = 'gdc_download_20231023_030720.404045.tar.gz'# 要解壓縮的 tar 檔案名稱
target_directory = 'destination_folder'# 解壓縮目標目錄
with tarfile.open(file_name, 'r') as tf:# 開啟檔案                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
    tf.extractall(path=target_directory)# 解壓縮檔案到指定目錄

OPENSLIDE_PATH = r'C:\path\to\bin'  #Windows安裝OpenSlide

import os
if hasattr(os, 'add_dll_directory'):
    
    with os.add_dll_directory(OPENSLIDE_PATH):
        import openslide
else:
    import openslide

import openslide   #導入套件
import os #檔案操作套件
import pandas as pd
from glob import glob #查找匹配檔案套件
from openslide import OpenSlide
from pprint import pprint  #美化print
import matplotlib.pyplot as plt

slide=openslide.OpenSlide(r"C:\Users\user\Desktop\31d9a30a-73e9-4506-8449-ae1ef517aed5\TCGA-23-1024-01A-01-BS1.7c5c688d-74e7-470a-95c5-115c73451c0d.svs") #讀取圖像

print(slide.dimensions) #圖像尺寸
print(slide.level_count) #圖像層數 #0等級從（最高解析度）到圖像（最低解析度）#以多個層級的金字塔結構進行存儲。每個層級都對應著圖像的不同分辨率，最底層的層級通常包含最高分辨率的圖像，而隨著層級的上升，圖像分辨率逐漸降低
print(slide.level_dimensions) #圖像的每個層級的尺寸
print(slide.level_downsamples)#降採樣#縮小圖像的尺寸
print(slide.get_best_level_for_downsample(2))#用於根據給定的降采樣比例找到最適合的層級

print(slide.properties)#有關投影片的元數據
pprint(dict(slide.properties))

print(slide.associated_images)#用於獲取與鏡片掃描圖像相關聯的其他圖像數據
#set_cache(cache)#方法是用於配置圖像讀取時的緩存，可以通過設置緩存的大小和其他相關參數，以提高對大型鏡片掃描圖像的處理效率

#print(slide.read_region)讀取圖像特定區域的方法
region = (0, 0) 
level = 2
size = (2000, 2000)
image = slide.read_region(region, level, size)
plt.figure(figsize=(20, 20))
plt.imshow(image)

thumbnail_size = (500, 500) #指定縮略圖的尺寸
thumbnail = slide.get_thumbnail(thumbnail_size)#使用 get_thumbnail 方法獲取縮略圖
thumbnail.show()# 顯示縮略圖

