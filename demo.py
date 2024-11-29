from PIL import Image

import pytesseract


img = Image.open('e697fd2b588d3a08d69b32f45da6965.png')

text = pytesseract.image_to_string(img,  lang='chi_sim')

print(text)
