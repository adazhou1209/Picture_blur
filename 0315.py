from PIL import Image, ImageFilter
import numpy as np

# 圖片物件指派給變數image --> 讀取圖片
image = Image.open(r'D:\base\cat.jpg')

# 定義掃描的核心塊 3*3 
# 1/9為將周圍值平均化
kernel = [1/9, 1/9, 1/9,
          1/9, 1/9, 1/9,
          1/9, 1/9, 1/9] 

# 取得image的圖片寬、高 
(width, height) = image.size

# 運用PIL套件方法創造一個新的影像
blurred_image = Image.new("RGB", (width, height))

# 掃描整張圖像的每個像素
for x in range(1, width-1):
    for y in range(1, height-1):
        # 獲取kernel內的顏色值
        pixels = []           # 空元素來更新每次的值
        for i in range(-1, 2):
            for j in range(-1, 2):
                pixels.append(image.getpixel((x+i, y+j)))
                #var.append()添加()中的值進入[]中
                #picture.getpixel(x,y) 讀取座標的"RGB"顏色值

        # 將kernel應用於像素顏色值
        
        r = sum(p[0] * kernel[i] for i, p in enumerate(pixels) )
        g = sum(p[1] * kernel[i] for i, p in enumerate(pixels) )
        b = sum(p[2] * kernel[i] for i, p in enumerate(pixels) )
        # p[0] --> 顏色通道
        # kernel[i+1 + 3*j] 表示kernel是一個3*3矩陣，矩陣每一行由平面中三個連續元素表示 
        # 其中 +1 為保證kernel中心像素對當前處理的RGB值進行加權
        # p in enumerate(pixels) --. enumerate為將可遍歷的數據組合成索引序列


        # 設置模糊圖像中的像素顏色
        blurred_image.putpixel((x, y), (int(r), int(g), int(b)))
        # picture.putpixel(self, xy, color)數據的讀取及訪問權限 

# 將模糊圖像保存到新文件
blurred_image.save("blurred_example.jpg")
#顯示模糊圖像
image.show()
blurred_image.show()


"""
var = Image.new(mode("RGB"), size("width, height"), color(數值))
pixels.append(image.getpixel((x+i, y+j)))
"""
