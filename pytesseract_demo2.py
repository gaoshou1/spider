import pytesseract
from urllib import request
from PIL import Image
import time

def main():
    pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract\tesseract.exe"
    url = 'https://login.sina.com.cn/cgi/pin.php?r=58339953&s=0&p=gz-b437272c7ee3e20eb56c914440338358c402'
    while True:
        request.urlretrieve(url, 'captcha.png')
        imge = Image.open('captcha.png')
        text = pytesseract.image_to_string(imge)
        print(text)
        time.sleep(2)






if __name__ == '__main__':
    main()