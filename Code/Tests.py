#Tests
import pandas as pd
import scipy.stats as stats


#Question1: Is the age restriction for movies on Disney+ lower than for movies on Netflix?
netflix_data = [0]*144 + [7]*322 + [13]*404 + [16]*151 + [18]*877
disney_data = [0]*370 + [7]*278 + [13]*70 + [16]*4 + [18]*3

u_statistic, p_value = stats.mannwhitneyu(disney_data, netflix_data, alternative='less')
print("Question1, Mann-Whitney U Test result: ", "U-Stat: ",u_statistic,"P-Value: ", p_value)

#Question2: Is there a difference in Rotten Tomatoes Score for movies on those two platforms?
dr = pd.read_csv("G:/Application/3/Data/DisneyRates.csv")
nr = pd.read_csv("G:/Application/3/Data/NetflixRates.csv")

u_statistic1, p_value1 = stats.ttest_ind(a=nr.NetflixRate, b=dr.DisneyRate, equal_var=True)
print("Question2, T-Test result: ", "U-Stat: ",u_statistic1,"P-Value: ", p_value1)
