#Tests
import pandas as pd
import scipy.stats as stats

#Question1: Is the age restriction for movies on Disney+ lower than for movies on Netflix?
disney_data = pd.read_csv("G:/Application/3/Data/DisneyAge.csv")
netflix_data = pd.read_csv("G:/Application/3/Data/NetflixAge.csv")

u_value, p_value = stats.mannwhitneyu(disney_data.DisneyAge, netflix_data.NetflixAge, alternative='less')
print("Question1: Is the age restriction for movies on Disney+ lower than for movies on Netflix?")
print(" Mann-Whitney U Test result: ", f"U-Value: {u_value:.5f},     P-Value: {p_value:.5f}")

#Question2: Is there a difference in Rotten Tomatoes Score for movies on those two platforms?
dr = pd.read_csv("G:/Application/3/Data/DisneyRates.csv")
nr = pd.read_csv("G:/Application/3/Data/NetflixRates.csv")

t_value, p_value = stats.ttest_ind(a=dr.DisneyRate, b=nr.NetflixRate, equal_var=False)
print(f"\n\nQuestion2: Is there any differences in Rotten Tomatoes Score between the two platforms?")
print(" T-Test result: ", f"T-Value: {t_value:.5f},     P-Value: {p_value:.5f}")

