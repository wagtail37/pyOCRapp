from PIL import Image
import pyocr

# OCRエンジンを取得
engines = pyocr.get_available_tools()
engine = engines[0]

# 画像の文字を読み込む
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
txt = engine.image_to_string(Image.open('imageSample.png'), lang="jpn",builder=builder)
print(txt) 