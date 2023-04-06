#Importing Libraries
#Importing Google Text to Speech library
from gtts import gTTS

#Importing PDF reader PyPDF2
import PyPDF2

#Open file Path
pdf_File = open('name.pdf', 'rb') 

#Create PDF Reader Object
pdf_Reader = PyPDF2.PdfFileReader(pdf_File)
count = pdf_Reader.numPages # counts number of pages in pdf
textList = []

****************************
#Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

#Set language to english (en)
language = 'en'

#Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

#Save as mp3 file
myAudio.save("Audio.mp3")
