# Importing required libraries
from pathlib import Path
import pandas as pd

# Store the path of the saved excel files
folder = r'C:\Users\Saturn\Onedot_task\Final_results'

# Looping through all xlsx files in the folder
files = [f for f in Path(folder).glob('*.xlsx')]

# Creating a combined excel workbook
writer = pd.ExcelWriter(f'{folder}\combined_excel_spreadsheet.xlsx')

# iterate through each excel file 
for file in files: 
    df = pd.read_excel(file)
    df.to_excel(writer,sheet_name=file.stem,index=False)

# Saving the combined excel file as final result
writer.save()