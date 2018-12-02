#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import pandas as pd
import os
import sys
dataToClean = pd.ExcelFile(sys.argv[1])
sheetData= dataToClean.sheet_names
df = pd.read_excel(dataToClean, sheetData[6])
# Drop the duplicates:
df_no_duplicate= df.drop_duplicates()
# Drop rows where all cells in that row is NAN
df_no_missing = df_no_duplicate.dropna(how='all')
# Replace all missing values with a string - 'Missing'
df_to_fill=df_no_missing.fillna('Missing', inplace=True)
# Drop irrelevent columns
df = df_no_missing
df = df.dropna(subset=[df.columns[1]])
df = df.drop(df.columns[5:], axis=1)
# Rename Unnamed columns
df = df.rename(index=str, columns={"Unnamed: 1": " اسماء الموارد", "Unnamed: 2": "قيمة الموارد" ,  })
# fill missing value
somme=0
nb=0
for row in range(len(df)):
    for cell in range(len(df.columns)):
        print(df[df.columns[cell]][row])
	# Detect Missing value
        if df[df.columns[cell]][row] == "Missing": 
		column_name = df.columns[cell]
		row_name = df[df.columns[1]][row]
		# Search all the value from other sources and do the mean
		for element in os.listdir('./saisie2018'):
			data = pd.ExcelFile(element)
			sheetData= dataToClean.sheet_names
			df_other = pd.read_excel(data, sheetData[6])
			df_other = df_other.dropna(subset=[df.columns[1]])
			df_other = df_other.drop(df.columns[5:], axis=1)
			df_other = df_other.rename(index=str, columns={"Unnamed: 1": " اسماء الموارد", "Unnamed: 2": "قيمة الموارد" ,  })
			Somme=Somme+df_other[df.columns[column_name]][column_name]
			nb=nb+1
		mean=somme/nb
	# Assigned the value 
	df[df.columns[cell]][row]=mean
df.to_csv("cleaning_"+argv[1], sep='\t', encoding='utf-8')
			

				

	

