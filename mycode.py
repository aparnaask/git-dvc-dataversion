import pandas as pd
import os

data = {'Name':['Alice','bob','charlie'],
        'Age': [25,30,35],
        'city':['mumbai','new york','delhi']}

df = pd.DataFrame(data)

# # adding new rows to df for v2
new_row_loc = {'Name':'G1','age':20,'city':'city1'}
df.loc[len(df.index)] = new_row_loc

# # adding new rows to df for v3
# new_row_loc = {'Name':'v3','age':30,'city':'city1'}
# df.loc[len(df.index)] = new_row_loc

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f'csv filed saved to {file_path}')