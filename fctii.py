import pandas as pd
import numpy as np
import csv
import sys

#to be changed with args
filename=sys.argv[1] 
null_symbol=sys.argv[2] #? or NULL
str_cols_arg=sys.argv[3] #? or NULL

input_table=pd.read_csv(f"{filename}.csv")

str_cols_defined=str_cols_arg.split(",") #split 3rd arg to a list of strings

temp_cols_str=[]
for col in str_cols_defined: #transform a list of cols name to their index
    try:
        temp_cols_str.append(int(col)-1) #for index columns used
    except:
        temp_cols_str.append(list(input_table.columns).index(col)) #for name of columns used
str_cols_defined=temp_cols_str

#csv modification
def query(table,string_cols): #string colscould be in index (int) or name of the column
    for i, row in table.iterrows():
        for j in range(table.shape[1]): #jadiin string
            if j in str_cols_defined:
                if table.iloc[i][j] != f'{null_symbol}':
                    table.iloc[i][j]=f'"{table.iloc[i][j]}"'
                else:
                    table.iloc[i][j] = 'NULL'
            if j == 0:
                table.iloc[i][j]='('+table.iloc[i][j]
            elif j == table.shape[1]-1:
                table.iloc[i][j]=table.iloc[i][j]+')'

                
query(input_table,str_cols_defined)
input_table['blank']=[None]*(input_table.shape[0]) #to get that last comma in every line
try:
    input_table.to_csv(f'{filename}.txt',index=False,header=False, quotechar='"',quoting=csv.QUOTE_NONE)
except:
    pass
#replace that last comma
my_file = open(f"{filename}.txt")
string_list = my_file.readlines()
my_file.close()

string_list[-1]=string_list[-1][:-2]+string_list[-1][-2:].replace(",", ";")

my_file = open(f"{filename}.txt", "w")
new_file_contents = "".join(string_list)
my_file.write(new_file_contents)
my_file.close()

#hurray
print(f'Text saved to {filename}.txt!')
