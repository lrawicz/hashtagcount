import re, time, sys, os
import urllib.request, urllib.parse
from dotenv import load_dotenv

def main(instagram,inputPath,outputPath):
	result= ""
	fileInput =  open(inputPath, 'r', encoding='UTF-8')
	hashtags = [x[:-1] for x in fileInput if x.split()]
	i = 0
	for hashtag in hashtags:
			hashtag = hashtag.replace("\n","")
			i=i+1
			print(str(i) + "/" + str(len(hashtags))) #progress bar
			if hashtag != "":
				url = instagram + urllib.parse.quote(hashtag) #hashtag.replace("ñ","%C3%B1")
				print(hashtag)
				print(url)
				#response = urllib.request.urlopen(url)
				html = urllib.request.urlopen(url).read()
				value = re.findall(r'edge_hashtag_to_media":{"count":[0-9]*',str(html))#[0][32:]
				value = value[0][32:]
				result = result + hashtag + "," + value + "\n"
	if os.path.exists(outputPath):
		os.remove(outputPath)
	fileOutput = open(outputPath, 'w+')
	fileOutput.write( result)
	fileOutput.close()
	fileInput.close()

if __name__ == "__main__":
	load_dotenv("dotenv")
	instagram  = os.getenv("INSTAGRAM")
	inputPath  = os.getenv("INPUT_PATH")
	outputPath = os.getenv("OUTPUT_PATH")
	main(instagram,inputPath,outputPath)