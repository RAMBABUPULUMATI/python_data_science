import pandas as pd
df = pd.read_csv('next_of_kin.csv',encoding= "ISO-8859-1")
#print(df['given_name'].unique())
print(df['given_name'][df['relationship']=='grandparent'])