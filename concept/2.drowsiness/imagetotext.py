from PIL import Image

import pytesseract

text=pytesseract.image_to_string(Image.open("img.png"))

print(text)

file=open("file.txt","w")
file.writelines(text)
file.close()