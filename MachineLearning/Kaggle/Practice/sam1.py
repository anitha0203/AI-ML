import numpy as np 
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file into a DataFrame
data = pd.read_csv('dataFiles/languages.csv')

# Get the top 10 languages by users
top_10_users = data[['title', 'number_of_users']].groupby('title').sum()

print(top_10_users.head())
top_10_users = top_10_users.nlargest(10, 'number_of_users')

# Get the top 10 languages by jobs
top_10_jobs = data[['title', 'number_of_jobs']].groupby('title').sum()
top_10_jobs = top_10_jobs.nlargest(10, 'number_of_jobs')

# Create two subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Plot 1: Top 10 by Users
axs[0].bar(top_10_users.index, top_10_users['number_of_users'], color='skyblue')
axs[0].set_title('Top 10 Languages by Users')
axs[0].set_ylabel('Number of Users')

# Plot 2: Top 10 by Jobs
axs[1].bar(top_10_jobs.index, top_10_jobs['number_of_jobs'], color='lightcoral')
axs[1].set_title('Top 10 Languages by Jobs')
axs[1].set_ylabel('Number of Jobs')

# Rotate x-axis labels for better readability
for ax in axs:
    ax.tick_params(axis='x', rotation=45)

# Adjust spacing between subplots
plt.tight_layout()

# Show the plots
plt.show()