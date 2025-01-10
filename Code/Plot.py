#Plots
import matplotlib.pyplot as plt
import pandas as pd

#Preparing data sets for age restrictions
netflix_data = [0]*144 + [7]*322 + [13]*404 + [16]*151 + [18]*877
disney_data = [0]*370 + [7]*278 + [13]*70 + [16]*4 + [18]*3

#Plot Age Restrictions on Netflix
plt.figure(figsize=(5, 4))
plt.hist(netflix_data, bins=[0, 7, 13, 16, 18, 20], edgecolor='black', alpha=0.7)
plt.title('Histogram of Age Restrictions for movies on Netflix')
plt.xlabel('Age Restriction')
plt.ylabel('Frequency')
plt.xticks([0, 7, 13, 16, 18])
plt.show()

#Plot Age Restrictions on Disney+
plt.figure(figsize=(5, 4))
plt.hist(disney_data, bins=[0, 7, 13, 16, 18, 20], edgecolor='black', alpha=0.7)
plt.title('Histogram of Age Restrictions for movies on Disney+')
plt.xlabel('Age Restriction')
plt.ylabel('Frequency')
plt.xticks([0, 7, 13, 16, 18])
plt.show()

#read from csv file
dr = pd.read_csv("G:/Application/3/Data/DisneyRates.csv")
#Plot Scores on Disney+
plt.figure(figsize=(9, 4))
plt.hist(dr.DisneyRate, bins=19,  edgecolor='black', alpha=0.7)
plt.title('Histogram of Rotten Tomatoes score for movies on Disney+')
plt.xlabel('Rotten Tomatoes score')
plt.ylabel('Frequency')
plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.show()

#read from csv file
nr = pd.read_csv("G:/Application/3/Data/NetflixRates.csv")
#Plot Scores on Netflix
plt.figure(figsize=(9, 4))
plt.hist(nr.NetflixRate, bins=19,  edgecolor='black', alpha=0.7)
plt.title('Histogram of Rotten Tomatoes score for movies on Netflix')
plt.xlabel('Rotten Tomatoes score')
plt.ylabel('Frequency')
plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.show()
