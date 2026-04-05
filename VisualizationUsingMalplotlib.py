import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Company Sales Data.csv")
def line_plot():
    plt.plot(df,label='Line 1',color='red',linestyle=':',linewidth=3,marker="o")
    plt.plot(df,label='Line 2',marker='o',linewidth=3)
    plt.title("Month-wise Profit")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.legend()
    plt.show()
line_plot()
def bar_graph():
    plt.bar(df,df)
    plt.title("Sales")
    plt.xlabel("Face Cream")
    plt.ylabel("Face Wash")
    plt.show()
bar_graph()