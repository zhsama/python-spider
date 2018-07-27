import pytesseract
import tesserocr
from PIL import Image

# ocr识别
image = Image.open('code.jpg')
# result = tesserocr.image_to_text(image)
# print(result)

# print(tesserocr.file_to_text('code2.jpeg'))

# 图片处理
# image = image.convert('L')
# image = image.convert('1')
# image.show()

# image = image.convert('L')
threshold = 100
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

image = image.point(table, '1')
image.show()
result = tesserocr.image_to_text(image)
print(result)