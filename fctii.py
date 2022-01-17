import pandas as pd
import numpy as np
import csv

#to be changed with args
filename='mapping_mbank_omni' 
null_symbol='?' #or NULL

input_table=pd.read_csv(f"{filename}.csv")

#csv modification
def query(table,string_cols): #string colscould be in index (int) or name of the column
    for i, row in table.iterrows():
        for j in string_cols: #jadiin string
            if table.iloc[i][j] != f'{null_symbol}':
                table.iloc[i][j]=f'"{table.iloc[i][j]}"'
            else:
                table.iloc[i][j] = 'NULL'
            if j == 0:
                table.iloc[i][j]='('+table.iloc[i][j]
            elif j == table.shape[1]-1:
                table.iloc[i][j]=table.iloc[i][j]+')'
                
query(input_table,[0,1,2])
input_table['blank']=[None]*(input_table.shape[0]) #to get that last comma in every line

input_table.to_csv(f'{filename}.txt',index=False,header=False, quotechar='"',quoting=csv.QUOTE_NONE)

#replace that last comma
my_file = open(f"{filename}.txt")
string_list = my_file.readlines()
my_file.close()

string_list[-1]=string_list[-1][:-2]+string_list[-1][-2:].replace(",", ";")

my_file = open(f"{filename}.txt", "w")
new_file_contents = "".join(string_list)
my_file.write(new_file_contents)
my_file.close()