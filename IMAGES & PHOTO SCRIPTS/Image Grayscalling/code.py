from os import getcwd, listdir
from os.path import isfile, join

from PIL import Image

onlyfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]
print("All files in current dir :",onlyfiles)

img = Image.open(input("Enter image filename : "))  # image name with relative path
grayscale = img.convert('L')
grayscale.save(f'GrayScaled_{img.filename}')

