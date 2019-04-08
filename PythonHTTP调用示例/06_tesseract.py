from PIL import Image
import pytesseract

file_path = ""  # 图片地址

img = Image.open(file_path)
pytesseract.image_to_string(img)

