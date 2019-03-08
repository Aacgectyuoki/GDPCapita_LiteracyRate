import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cb.csv')
fig, ax = plt.subplots()
cb_csv = ax.scatter(df["GDP (IMF)"], df["Amount"])
   
ax.set_xlabel("GDP")
ax.set_ylabel("Literacy Rate %")
    
plt.show()
