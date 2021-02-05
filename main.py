import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\\Users\\njlowhorn\\Desktop\\Most Popular Programming Languages from 2004 to 2020 V2.csv')

jul_df = df[df["Date"].str.contains("Jul")]
values = jul_df[["Date", "Python"]]

print(df.head(3))

ax = values.plot.bar(x="Date", y="Python", color="k")
plt.xlabel('Dates')
plt.ylabel('% of Programmers')
plt.title('Percentage of Programmers Using Python Over Time')
plt.tight_layout()
ax.set_facecolor('purple')

plt.show()

