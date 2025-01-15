#Plots
import matplotlib.pyplot as plt
import pandas as pd

#Preparing data sets for age restrictions
netflix_data = {'(0-20)': 1.46, '(21-40)': 12.74, '(41-60)': 55.12, '(61-80)': 26.68, '(81-100)': 3.99}

#Plot Age Restrictions on Netflix
plt.figure(figsize=(5, 4))
plt.bar(list(netflix_data.keys()), list(netflix_data.values()))
plt.title('Relative Frequency for Rotten Tomatoes Score on Netflix')
plt.xlabel('Rotten Tomatoes Score')
plt.ylabel('Relative Frequency (percent)')
plt.xticks(["(0-20)", "(21-40)", "(41-60)", "(61-80)", "(81-100)"])
plt.show()

#Preparing data sets for age restrictions
disney_data =  {'0+': 51.03, '7+': 38.34, '13+': 9.66, '16+': 0.55, '18+': 0.41}
netflix_data = {'0+': 7.59, '7+': 16.97, '13+': 21.29, '16+': 7.96, '18+': 46.21}

#Plot Age Restrictions on Disney+
plt.figure(figsize=(5, 4))
plt.bar(list(disney_data.keys()), list(disney_data.values()))
plt.title('(a) Relative Frequency for Age Restrictions on Disney+')
plt.xlabel('Age Restriction')
plt.ylabel('Relative Frequency (percent)')
plt.xticks(["0+", "7+", "13+", "16+", "18+"])
plt.show()

#Plot Age Restrictions on Netflix
plt.figure(figsize=(5, 4))
plt.bar(list(netflix_data.keys()), list(netflix_data.values()))
plt.title('(b) Relative Frequency for Age Restrictions on Netflix')
plt.xlabel('Age Restriction')
plt.ylabel('Relative Frequency (percent)')
plt.xticks(["0+", "7+", "13+", "16+", "18+"])
plt.show()

#read from csv file
dr = pd.read_csv("G:/Application/3/Data/DisneyRates.csv")
nr = pd.read_csv("G:/Application/3/Data/NetflixRates.csv")

#Plot Scores on Disney+
plt.figure(figsize=(9, 4))
plt.hist(dr.DisneyRate, bins=19,  edgecolor='black', alpha=0.7)
plt.title('(a) Histogram of Rotten Tomatoes score for movies on Disney+')
plt.xlabel('Rotten Tomatoes Score')
plt.ylabel('Frequency')
plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.show()

#Plot Scores on Netflix
plt.figure(figsize=(9, 4))
plt.hist(nr.NetflixRate, bins=19,  edgecolor='black', alpha=0.7)
plt.title('(b) Histogram of Rotten Tomatoes score for movies on Netflix')
plt.xlabel('Rotten Tomatoes Score')
plt.ylabel('Frequency')
plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.show()



