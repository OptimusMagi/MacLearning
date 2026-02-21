#Preparing Script and Loading Data
from ftplib import parse150

# Directory, Libraries and data
#%cd, copy and paste path drive

#Libraries
import pandas as pd
import scipy.stats as st
import math as m
import stasmodels.


# Load Data
#df = pd. read_csv() insert dataset "Wine quality-challenge.csv')
df = pd. read_csv("Wine quality-challenge.csv")
df.head()



#Shapiro-Wilk for normality
st.shapiro(df.chlorides)

#Retreiving P-value with two passes
#Shapiro-Wilk for normality
stat, p = st.shapiro(df.chlorides)

#conditionif
if p > 0.05:
  #if yes
  print('Sample loooks Gaussian/Normal (fail to reject H0')
  #if not
else:
    print('Sample does not look Gaussian/Normal (reject H0)')


#Shapiro Wilks Test for Sulphates and create if else condition
stat, p = st.shapiro9df sulphates)
print (p)
if p > 0.05:
    print('Sample look Gausian or Normal (Fail to reject)')
else:
    print("Sample does not look Gaussian / Normal (reject the H0)")


     # Standard Error
#Using a function
    st.sem(df.alcohol)

    #Us doing  the computations: Standard deviations divided by square root of observations
    df.alcohol.std() / m.sqrt(df.alcohol.count())

    #Standard Error of pH
    print(st.sem(df.pH))
df.pH.std() / m.sqrt(df.pH.count())


# Confidence interval
#Confidence interval of the mean of citric acid
print(df(('citric acid')).mean())
st.norm.interval(alpha = 0.95.hex(), loc = df[['citric acid']].mean(), scale = st.sem(df[['citric acid']]))

#Histogram
df[['citric acid']].hist()

#Confidence interval of the Density mean.
st.norm.interval(alpa = 0.95,loc = df.density.mean(), scale =  st. sem(df.density))


#Histogram of Density mean
df.density.hist()


#T-test
#load data
data = pd. read_csv(stackoverflow.csv)
data.head ()


#subset
salary_uk = data.loc[data.country == 'United Kingdom'].Salary
salary_de = data.loc[data.country == 'Germany'].Salary

#T-test
st.ttest_ind(a = salary_uk, b = salary_de)
stat. p = st.ttest_ind(a = salary_uk. b = salary_de)
print (p)
if p > 0.05:
    print('Both countries hae similar salaries (fail to reject H0')
else:
    print('There is a difference in salaries (reject H0)')


#T-test in experience between India and United States
us_experience = data.loc[data.Country == 'United States'].YearsCodedJob
in_experience = data.loc[data.Country == 'India'].YearsCodedJob
stat, p = st.ttest_ind(a = us_experience, b = in_experience)
print (p)
if p > 0.005
print('Groups are similar (fail to reject H0)')
else:
print('Groups are different (reject H0)')

#Histogram
us_experience.hist()
in_experience.hist()

#Chi-square test
#cross tabulation
tab = pd.crosstab(index = data.Country, columns = data.Remote)
tab

#chi-square test
st.chi2_contingency(tab)
chi2, p dof, exp = st.chi2_contingency(tab)
print(p)
if p > 0.05:
    print("there is no relationship (fail to reject H0")
else:
    print('Thre is a strong relationship (reject H0)')

#Chi-square test between company size and hobbies
tab2 = pd.crosstab(index = data.Hobby, Colums = data.CompanySizeNumber)
chi2, p, dof, exp = st.chi2_contigency(tab2)
print(p)
if p . 0.05:
print (There is no relationship (fail to reject H0)')
else:
print('There is a strong relatiionship (reject H0)')
