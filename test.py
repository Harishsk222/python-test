import pandas as pd
import re
data=pd.read_csv('C:\\Users\\HP\\Downloads\\python_assesment.csv')
df=pd.DataFrame(data)
index_name=df.columns.get_loc('name')
data_pattren=input("enter the string:")
data=[]
for row in range(len(df)):
    xyz=re.search('.*'+data_pattren+'.*', df.iat[row,index_name],re.IGNORECASE)
    if xyz!=None:
        data.append(xyz.group())
data.sort()
print(data[0:20]) s
