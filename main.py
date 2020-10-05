import pyttsx3
import PyPDF2

book = open('jor.pdf', 'rb')
print(book)
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
""" page = pdfreader.getPage(5)
text = page.extractText()
print(text) """
eng = pyttsx3.init()
for num in range(1, pages):
    page = pdfreader.getPage(num)
    text = page.extractText()
    eng.say(text)
    eng.runAndWait()
