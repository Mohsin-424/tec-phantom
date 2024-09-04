#...................... pip install Openpyxl-->for  dealing with Excel CSV files in Python ................

import csv
# Open the File
data = open("data.csv" , encoding = "utf-8")
# CSV Reader
csv_data = csv.reader(data)
# Reformat it into a Python Object  List of Lists
data_lines = list(csv_data)
print(data_lines)
  


import pyPDF2
