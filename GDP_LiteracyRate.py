import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('cb.csv') #combination of the 
# literacy rate and GDP files

fig, ax = plt.subplots()
cb_csv = ax.scatter(df["GDP Per Capita"], df["Amount"])
   
ax.set_xlabel("GDP Per Capita")
ax.set_ylabel("Literacy Rate %")
    
plt.show()
