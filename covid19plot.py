#import libraries
import pandas as pd
import matplotlib.pyplot as plt

#make a data frame from the csv file
df = pd.read_csv('covid19countries.csv')

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

ax.grid(True)
ax.set_xticks([0, 3, 6, 9, 11, 13])

ax.set_xticklabels(['Apr 8', 'Apr 11', 'Apr 13', 'Apr 16', 'Apr 19', 'Apr 21'])

plt.style.use('seaborn-pastel')

plt.title('Covid-19 Cases April 8-21', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Number of Cases')

plt.plot(df['Italy'], linewidth=6, label='Italy')
plt.plot(df['France'], linewidth=6, label='France')
plt.plot(df['Iran'], linewidth=6, label='Iran')
plt.legend()

plt.savefig('covid19-apr8-21.png')