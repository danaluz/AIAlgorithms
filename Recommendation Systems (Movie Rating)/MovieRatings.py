import numpy as np
import collections
import pandas
# Import the ratings for the file
with open("A1Ratings.csv", 'r') as csvfile:
    ratings = pandas.read_csv(csvfile)


def mean (column):
    value = (column.sum()) / len(column)
    return round(value,2);

def percentage (column):
    counter = collections.Counter(column)
    value = ((counter[4]+counter[5])*100)/len(column)
    return round(value,2);

def distance(longColumnTargetOriginal, columnTarget, column1):
    compare = (columnTarget & column1)
    counting = list(filter(lambda x: x == True, compare))
    counting = len(counting)
    value = (counting / longColumnTargetOriginal) * 100
    return round(value,2);

def printingSortedBy (criteria, data):
    print("Printing Sorted by: ", criteria)
    sortedRatings = data.sort_values(by=criteria, ascending=False)
    print(sortedRatings)
    return;

#-------------------------------------------------------------------------------------------------------------

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
    pepe1.append(mean(ratingsColumn))
    pepe2.append(ratingsColumn.name[:20]+'...')
    pepe3.append(len(ratingsColumn))
    pepe4.append(percentage(ratingsColumn))
    pepe5.append(distance(long, comparison1, ratingsColumn))

# Creating a new DataFrame
d= {'Percentages' : pepe4, 'Name': pepe2, 'Mean': pepe1, 'Ratings': pepe3, 'Distance': pepe5}
df = pandas.DataFrame(d)
# Elimination of the first row
df.drop(df.index[[0]], inplace=True)
# Reordering the Columns
df = df[['Name', 'Percentages','Mean','Ratings', 'Distance']]

#Printing..
printingSortedBy('Percentages', df)


