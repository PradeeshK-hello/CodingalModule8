import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
df = pd.read_csv("Iris Dataset.csv")
def barplot():
    plt.bar(df)
    plt.title("Bar Plot")
    plt.xlabel("Species")
    plt.ylabel("SepalLengthCm")
    plt.show()
barplot()
def countplot():
    sns.countplot("Species")
    plt.title("Count of Species")
countplot()
def boxplot():
    sns.boxplot(df)
    plt.xlabel("Species")
    plt.ylabel("SepalWidthCm")
    plt.show()
boxplot()
def swarmplot():
    sns.swarmplot(df)
    plt.xlabel("Species")
    plt.ylabel("SepalWidthCm")
    plt.show()
swarmplot()
def distplot_jointplot():
    sns.distplot("SepalWidthCm")
    sns.jointplot("SepalWidthCm")
distplot_jointplot()
def pairplot():
    sns.pairplot(df,hue="species")
pairplot() 