from PIL import Image, ImageFilter
import numpy as np

# 圖片物件指派給變數image --> 讀取圖片
image = Image.open(r'E:\cute cat.jpg')

# 定義掃描的核心塊 3*3 
kernel = [0, -1, 0,
          -1, 5, -1,
          0, -1, 0 ]

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
        # p[ ] --> 顏色通道 r , g, b 
        #將3*3的通道顏色值求和，並且進行卷積處理

        # 設置模糊圖像中的像素顏色
        blurred_image.putpixel((x, y), (int(r), int(g), int(b)))
        #將上方卷積後處理的影像，儲存其模糊後的顏色

# 將模糊圖像保存到新文件
blurred_image.save("sharpen_example.jpg")
#顯示模糊圖像
image.show()
blurred_image.show()
