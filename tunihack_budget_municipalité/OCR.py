from PIL import Image
import pytesseract  
import os.path    
import io
import os
import json
import sys

path=sys.argv[1]
image = Image.open(path)
from PIL import ImageEnhance
amelioration = ImageEnhance.Sharpness(image)
resultat = amelioration.enhance(0.95)
text = pytesseract.image_to_string(resultat, lang = 'eng+ara')

fichier = open("C:/Users/Lenovo/Desktop/tunihack/tst.txt", "w",encoding='utf-8')
fichier.write(text)
fichier.close() 