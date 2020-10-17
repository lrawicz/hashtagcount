import os
from dotenv import load_dotenv
import codecs
load_dotenv("files/dotenv")
inputPath = os.getenv("INPUT_PATH")
print (inputPath)
fileInput = codecs.open(inputPath, encoding='UTF-8')
lista= [x for x in fileInput if x.split()]
for x in lista:
	print(x.replace("\n",""))
	pass