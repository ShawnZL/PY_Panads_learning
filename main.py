import pandas as pd
import json
from glom import glom
"""
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)
"""
"""
a = ['Google', 'Runoob', 'wiki']
myvar = pd.Series(a, index = ['x', 'y', 'z'])
print(myvar)
"""
"""
sites = {1: 'Google', 2: 'Runoob', 3: 'wiki'}
myvar = pd.Series(sites)
print(myvar)
"""
"""
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
df = pd.DataFrame(data, columns=['Site', 'Age'], dtype='float64')
print(df)
"""
"""
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print(df)
"""
"""
data = [{'a':1, 'b':2}, {'a': 5, 'b':10, 'c':20}]
df = pd.DataFrame(data)
print(df)
"""
"""
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)

# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
#返回1 2行
print(df.loc[[0,1]])
"""
"""
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# 指定索引
print(df.loc["day2"])
"""
"""
df = pd.read_csv('nba.csv')
print(df.to_string())
"""
"""
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]
# 字典
dict = {'name': nme, 'site': st, 'age': ag}
df = pd.DataFrame(dict)
# 保存 dataframe
df.to_csv('site.csv')
"""
"""
df = pd.read_csv('nba.csv')
#print(df.head(10).to_string())
#print(df.tail(5).to_string())
print(df.info())
"""
"""
df = pd.read_json('site.json')
print(df.to_string())
"""
"""
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}
df = pd.DataFrame(s)
print(df)
"""
"""
URL = 'https://static.runoob.com/download/sites.json'
df = pd.read_json(URL)
print(df)
"""
"""
df = pd.read_json('abs.json')
print(df)
"""

# JSON 模块载入数据

#with open('abs.json', 'r') as f:
#    data = json.loads(f.read())
# 展平数据
#df_nested_list = pd.json_normalize(data, record_path=['students'], meta=['school_name', 'class'])
#print(df_nested_list)
"""
with open('abc.json', 'r') as f:
    data = json.loads(f.read())

df = pd.json_normalize(
    data,
    record_path=['students'],
    meta=[
        'class',
        ['info', 'president'],
        ['info', 'contacts', 'tel']
    ]
)
print(df.to_string())
"""
"""
df = pd.read_json('abg.json')
data = df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)
"""
"""
missing_values = ["n/a", "na", "--"]
df = pd.read_csv('property-data.csv', na_values = missing_values)
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())
#print (df['NUM_BEDROOMS'])
#print (df['NUM_BEDROOMS'].isnull())
"""
#df = pd.read_csv('property-data.csv')
#new_df = df.dropna()
#new_df = df.dropna(subset=['ST_NUM'])
#new_df = df['PID'].fillna(12345)
#print(df.to_string())
#x = df['ST_NUM'].mean()
#new_df = df['ST_NUM'].fillna(x)
"""
x = df['ST_NUM'].median()
new_df = df['ST_NUM'].fillna(x)
print(new_df.to_string())
"""
"""
person = {
"name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}
df = pd.DataFrame(person)
#df.loc[2, 'age'] = 30 #修改数据
for x in df.index:
  if df.loc[x, "age"] > 120:
    df.drop(x, inplace = True)
print(df.to_string())
"""
person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df = pd.DataFrame(person) 
df.drop_duplicates(inplace = True)
print(df)

