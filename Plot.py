import matplotlib.pyplot as plt
import pandas as pd

netflix_data = [0]*144 + [7]*322 + [13]*404 + [16]*151 + [18]*877
disney_data = [0]*370 + [7]*278 + [13]*70 + [16]*4 + [18]*3

plt.figure(figsize=(12, 6))
plt.hist(netflix_data, bins=[0, 7, 13, 16, 18, 20], edgecolor='black', alpha=0.7)
plt.title('Histogram of Age Restrictions on Netflix')
plt.xlabel('Age Restriction')
plt.ylabel('Frequency')
plt.xticks([0, 7, 13, 16, 18])
plt.show()

plt.figure(figsize=(12, 6))
plt.hist(disney_data, bins=[0, 7, 13, 16, 18, 20], edgecolor='black', alpha=0.7)
plt.title('Histogram of Age Restrictions on Disney+')
plt.xlabel('Age Restriction')
plt.ylabel('Frequency')
plt.xticks([0, 7, 13, 16, 18])
plt.show()

##################################
dr = pd.read_csv("C:/Users/Sed/Desktop/Application/3/Data/DisneyRates.csv")
plt.figure(figsize=(12, 6))
plt.hist(dr.DisneyRate, bins=19,  edgecolor='black', alpha=0.7)
plt.title('Histogram of Rates on Disney')
plt.xlabel('Rate')
plt.ylabel('Frequency')
plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.show()

nr = pd.read_csv("C:/Users/Sed/Desktop/Application/3/Data/NetflixRates.csv")
plt.figure(figsize=(12, 6))
plt.hist(nr.NetflixRate, bins=19,  edgecolor='black', alpha=0.7)
plt.title('Histogram of Rates on Netflix')
plt.xlabel('Rate')
plt.ylabel('Frequency')
plt.xticks([10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
plt.show()
