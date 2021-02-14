{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. Python script for excel file creation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing required libraries\n",
    "from pathlib import Path\n",
    "import pandas as pd\n",
    "\n",
    "# Store the path of the saved excel files\n",
    "folder = r'C:\\Users\\Saturn\\Onedot_task\\Final_results'\n",
    "\n",
    "# Looping through all xlsx files in the folder\n",
    "files = [f for f in Path(folder).glob('*.xlsx')]\n",
    "\n",
    "# Creating a combined excel workbook\n",
    "writer = pd.ExcelWriter(f'{folder}\\combined_excel_spreadsheet.xlsx')\n",
    "\n",
    "# iterate through each excel file \n",
    "for file in files: \n",
    "    df = pd.read_excel(file)\n",
    "    df.to_excel(writer,sheet_name=file.stem,index=False)\n",
    "\n",
    "# Saving the combined excel file as final result\n",
    "writer.save()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
