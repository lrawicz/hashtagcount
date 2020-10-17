import csv
from dotenv import load_dotenv
import os
from openpyxl import Workbook, load_workbook
import datetime 

def main(csvFile, excel, sheet ):
    current_time = datetime.datetime.now()
    day = "000" + str(current_time.day)
    month = "000" + str(current_time.month)
    time_value = str(current_time.year) + "-" + month[-2:] + "-" + day[-2:]
    
    wb = load_workbook(excel)
    ws = wb[sheet]
    with open(csvFile) as f:
        reader = csv.reader(f, delimiter=',')
        print(reader)
        for row in reader:
            row.append(time_value)
            print(row)
            ws.append(row)
    wb.save(excel)

if __name__ == "__main__":
    load_dotenv("dotenv")

    excel = os.getenv("EXCEL")
    sheet = os.getenv("SHEET")
    outputPath = os.getenv("OUTPUT_PATH")
    
    main(outputPath, excel, sheet )