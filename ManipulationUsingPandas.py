import pandas as pd
dictionary = {"name": ["Pankaj","Meghna","David","Lisa"],\
    "roll": ["CEO",pd.NA,pd.NA,pd.NA],\
    "salary": ["100","200",pd.NA,pd.NA]}
labels = ["A","B","C","D"]
df = pd.DataFrame(dictionary,index=labels)
print(df.head(2))
print(df.tail(2))
null_count = df.isna().sum()
print(null_count)
print("Detailed Dataframe:","\n",df.info())
new_df = df.dropna()
print(new_df)
new_df2 = df.dropna(axis=1)
print(new_df2)
df["salary"] = df["salary"].fillna(300)
print(df.info())
df["roll"] = df["roll"].fillna("CEO")