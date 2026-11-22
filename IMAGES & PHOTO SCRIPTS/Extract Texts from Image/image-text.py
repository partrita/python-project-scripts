import os
import signal
import sys

import pytesseract
from PIL import Image


def handler(signum, frame):
    print("Text extraction script exited!")
    sys.exit(1)

signal.signal(signal.SIGINT, handler)

directory = os.fsencode(r"image files directory")
directory_in_str = r"image files directory"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith((".img", ".jpeg", ".jpg")):
        image = os.path.join(directory_in_str, filename)

        # check Program Files(x86) for tesseract.exe (Windows machines)
        pytesseract.pytesseract.tesseract_cmd = r"tesseract.exe directory"

        text = pytesseract.image_to_string(Image.open(image), lang="eng")
        with open("output.txt", "a", encoding='utf-8') as o:
            print(os.path.basename(image) + "\r" + os.path.basename(image) + " done")
            o.write('\n\n\n[NEW IMAGE]\n')
            o.write(image)
            o.write('\n')
            o.write(text)
        continue
    else:
        continue

print("Text extract script completed!")