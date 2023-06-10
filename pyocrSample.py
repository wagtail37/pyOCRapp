# from PIL import Image
# import pyocr
# import os
# import pyocr.builders

# # pyocr.get_available_tools()のエラーの解消
# pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# path = 'C:\Program Files\Tesseract-OCR'
# os.environ['PATH'] = os.environ['PATH'] + path
# tools = pyocr.get_available_tools()
# tool = tools[0]
# img = Image.open("Receipt2.png")
# builder = pyocr.builders.TextBuilder(tesseract_layout=6)
# text = tool.image_to_string(img, lang="jpn", builder=builder)
# text = text.replace(' ', '')
# print(text)

from PIL import Image
import pyocr

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 画像の文字を読み込む
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
txt = engine.image_to_string(Image.open('imageSample.png'), lang="jpn",builder=builder)
print(txt) 