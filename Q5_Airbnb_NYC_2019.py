import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

fileName = "./file/Airbnb_NYC_2019.csv"
df = pd.read_csv(fileName, low_memory=False)

topHost = df.groupby(['host_id']).name.count()
topHost = topHost.sort_values(ascending=False).head(10)

# visulization
fig = plt.figure()
sns.set(rc={'figure.figsize': (15, 9)})
plot1 = topHost.plot(kind='bar', width=0.7, color=['g', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'c', 'c'])
plot1.set_title('topHost', fontsize=15, color='b', fontweight='bold')
plot1.set_xlabel("Hosts's ID")
plot1.set_ylabel('Num of Listings')
plot1.set_xticklabels(plot1.get_xticklabels(), rotation=30)
plt.savefig('topHost.png')

# violinplot
df = df[df.price < 1000]
fig = plt.figure()
violinplot = sns.violinplot(data=df, x='neighbourhood_group', y='price')
violinplot.set_title('Price Distribution of group', fontsize=15, color='b', fontweight='bold')
violinplot
plt.savefig('Price Distribution of group.png')

# boxplot
fig = plt.figure()
boxplot = sns.boxplot(x='neighbourhood_group', y='price', data=df, showfliers=False)
boxplot.set_title('Price distribution of different group', fontsize=15, color='b', fontweight='bold')
boxplot
plt.savefig('Price distribution of different group.png')

# longitude and latitude across listings
plot2 = df.plot(figsize=(10, 8), kind='scatter', x='longitude', y='latitude', marker='.', label='availability_365',
                c='price', cmap=plt.get_cmap('jet'), colorbar=True)
plot2.set_title('Listing distribution', fontsize=15, color='b', fontweight='bold')
plot2
plt.savefig('Listing distribution.png')

# the relationship btw room_type and price
pivot_table2 = df.pivot_table(values='price', index='neighbourhood_group', columns='room_type',
                              aggfunc='mean').plot.bar()
pivot_table2.set_ylabel('Price', color='b', fontsize=13)
pivot_table2.set_xlabel('Neighbourhood_group', color='b', fontsize=13)
pivot_table2.set_xticklabels(pivot_table2.get_xticklabels(), rotation=45)
pivot_table2.set_title('Average Price by Room Type', fontsize=15, color='b', fontweight='bold')
plt.savefig('Average Price by Room Type.png')

# check the number of listings by Room Type across zone
pivot_table3 = df.pivot_table(values='price', index='neighbourhood_group', columns='room_type',
                              aggfunc='count').plot.bar()
pivot_table3.set_xlabel('Neighbourhood_group', color='b', fontsize=13)
pivot_table3.set_ylabel('Num of listings', color='b', fontsize=13)
pivot_table3.set_xticklabels(pivot_table2.get_xticklabels(), rotation=45)
pivot_table3.set_title('listing by Room Type', fontsize=15, color='b', fontweight='bold')
plt.savefig('listing by Room Type.png')

# Availability according to different room_type in different areas
fig5 = sns.catplot(x='neighbourhood_group', y='availability_365', kind='box', hue='room_type', data=df,
                   palette='pastel')
fig5.fig.suptitle('most popular area', fontsize=15, y=1.05)
fig5
fig5.savefig('most popular area.png', bbox_inches='tight')

# Price according to different room_type in different areas
fig6 = sns.catplot(x='neighbourhood_group', y='price', data=df, kind='bar', hue='room_type', palette='pastel')
fig6.fig.suptitle('most expensive area', fontsize=15, y=1.05)
fig6
fig6.savefig('most expensive area.png', bbox_inches='tight')
