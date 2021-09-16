# Data Set Version 2 by Nolan Lowhorn
# 9/16/2021

# Imports
import pandas as pd
import matplotlib.pyplot as plt

# Reads data
df = pd.read_csv(r'C:\Users\njlowhorn\PycharmProjects\DataSetProject\Most Popular Programming Languages from 2004 to 2020 V2.csv')

# Gets Python use in July
jul_df = df[df["Date"].str.contains("Jul")]
values = jul_df[["Date", "Python"]]

# Creates graph
ax = values.plot.bar(x="Date", y="Python", color="k")
plt.xlabel('Dates')
plt.ylabel('% of Programmers')
plt.title('Percentage of Programmers Using Python Over Time')
plt.tight_layout()
ax.set_facecolor('purple')

# Shows graph
plt.show()