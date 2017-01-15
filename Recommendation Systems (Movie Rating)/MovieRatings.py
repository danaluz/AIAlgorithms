import numpy as np
import collections
import pandas
# Import the ratings for the file
with open("A1Ratings.csv", 'r') as csvfile:
    ratings = pandas.read_csv(csvfile)

# Declaring some arrays
pepe1 = []
pepe2 = []
pepe3 = []
pepe4 = []
pepe5 = []

# Cleaning some of the data
ratingsMovieTarget = ratings["260: Star Wars: Episode IV - A New Hope (1977)"]
comparison1 = ~np.isnan(ratingsMovieTarget)
# Lenght of comparison
long = len(ratingsMovieTarget[comparison1])

# Evaluatins by Movies
for i in ratings:
    ratingsColumn = ratings[i]
    ratingsColumn = ratingsColumn[~np.isnan(ratingsColumn)]
    mean = (ratingsColumn.sum())/len(ratingsColumn)
    counter = collections.Counter(ratingsColumn)
    percentage = ((counter[4]+counter[5])*100)/len(ratingsColumn)
    compare = (comparison1 & ratingsColumn)
    counting = list(filter(lambda x: x == True, compare))
    counting = len(counting)
    porcent = (counting / long) * 100
    pepe1.append(round(mean,2))
    pepe2.append(ratingsColumn.name[:20]+'...')
    pepe3.append(len(ratingsColumn))
    pepe4.append(round(percentage, 2))
    pepe5.append(round(porcent, 2))

# Creating a new DataFrame
d= {'Percentages' : pepe4, 'Name': pepe2, 'Mean': pepe1, 'Ratings': pepe3, 'Distance': pepe5}
df = pandas.DataFrame(d)
# Elimination of the first row
df.drop(df.index[[0]], inplace=True)
# Reordering the Columns
df = df[['Name', 'Percentages','Mean','Ratings', 'Distance']]


#Sort by Percentages
testPercentages = df.sort_values(by='Percentages', ascending=False)

#Printing..
print(testPercentages)

#Sort by Mean
testMean = df.sort_values(by='Mean', ascending=False)

#Printing..
print(testMean)

#Sort by Ratings
testRatings = df.sort_values(by='Ratings', ascending=False)

#Printing..
print(testRatings)

#Sort by Distance
testDistance = df.sort_values(by='Distance', ascending=False)

#Printing..
print(testDistance)

