import pytesseract

from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe"

imge = Image.open('123.png')

text = pytesseract.image_to_string(imge, lang='chi_sim')  # chi_sim中文

print(text)