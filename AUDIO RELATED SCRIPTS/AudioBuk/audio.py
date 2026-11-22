from tkinter.filedialog import *

import PyPDF2
import pyttsx3

book = askopenfilename()
pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages

for num in range(pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speak = pyttsx3.init()
    speak.say(text)
    speak.runAndWait()