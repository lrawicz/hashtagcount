from dotenv import load_dotenv
import os
from openpyxl import Workbook, load_workbook
from src import hashtag, excel
def main():
	load_dotenv("dotenv")

	instagram = os.getenv("INSTAGRAM")
	outputPath = os.getenv("OUTPUT_PATH")
	inputPath = os.getenv("INPUT_PATH")
	excelFile = os.getenv("EXCEL")
	sheet = os.getenv("SHEET")

	hashtag.main(instagram,inputPath,outputPath)
	excel.main(outputPath, excelFile, sheet)

if __name__ == "__main__":
	main()