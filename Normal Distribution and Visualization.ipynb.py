#Density plot of Chlorides
df.chlorides.plot.density ()










#Check the # of observation within X standard deviations
df.loc(df.chlorides <= df.chlorides.mean() + 1 *df.chlorides.std())]
#set second one
df.loc(df.chlorides .>= df.chlorides.mean() + 1 * df.chlorides.std()) &
(df.chlorides.mean() -1 * df.chlorides.std())].chlorides.count()/ df.chlorides.count()


#68-95-99 check
df.loc[(df.chlorides <= df.chlorides.mean)]





# Try for 2 AND 3 'STANDARD DEVIATION' of above dataframe code

#ASSIGNMENT:
# Find what is the share of observations within 3 standard deviations of alcohol


df.alcohol.plot.density()
