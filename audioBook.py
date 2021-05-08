# modules needed
# pyttsx3
# pip install pyttsx3
# winshell
# pip install winshell
# pyPDF2
# pip install pyPDF2
import pyttsx3
import winshell
import PyPDF2
book = open("sample.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
for num in range(14, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
