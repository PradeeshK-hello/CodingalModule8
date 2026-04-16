import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv("IMDB Dataset.csv")
print(df.head(3),df.tail(3))
df.info()
df.isna()
new_df = df.loc[41:75]
print(df.max("No_of_votes"))
def boxplot():
    sns.boxplot(df)
    plt.xlabel("IMDB_Rating")
    plt.ylabel("Runtime")
boxplot()
def lineplot():
    plt.plot(df)
    plt.xlabel("IMDB_Rating")
    plt.ylabel("Runtime")
lineplot()
def distplot():
    sns.distplot(df)
    plt.xlabel("IMDB_Rating")
    plt.ylabel("Runtime")
distplot()
def countplot():
    sns.countplot("Runtime")
    plt.title("Particular Rating")
countplot()