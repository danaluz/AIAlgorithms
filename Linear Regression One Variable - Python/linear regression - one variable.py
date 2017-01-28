import pandas
import math as mt
import numpy as np
import matplotlib.pyplot as plt

def computeCost(X, y, theta):
    m = len(y)
    n=0.0
    for i in range(0,m):
        n += (theta[0]+ theta[1]*X[i] - y[i]) ** 2
    J = (1 / (2 * m)) * n
    return J;


def gradientDescent(X, y, theta, alpha, num_iters):
    m = len(y)
    J_history = np.zeros(num_iters);
    n = 0.0
    temp2=0.0
    temp1=0.0
    for i in range(0,num_iters):
        n1=0
        n2=0
        for i in range(0,m):
            n1 += (theta[0] + theta[1] * X[i] - y[i]);
            n2 += (theta[0] + theta[1] * X[i] - y[i]) * X[i];
        temp1 = theta[0] - (alpha) * (1 / m) * n1;
        temp2 = theta[1] - (alpha) * (1 / m) * n2;
        theta[0] = temp1;
        theta[1] = temp2;
        J_history[i] = computeCost(X, y, theta)

    return (theta,J_history);



#------------------------------------------------------ Start of Programa --------------------------------------------------------

# Opening the data set, and creating a DataFrame.
# The first columns correspond to the population of a City, and the second column correspond to the profit of a food truch in that city.
# A negative value for profit indicates a loss

with open("ex1data1.txt", 'r') as csvfile:
    ex1 = pandas.read_csv(csvfile)

df = pandas.DataFrame(ex1)

# Ploting our data set
x = df["City Population"].as_matrix()
y = df["Profit of Food Truck"].as_matrix()


#Computing the cost
size = len(y)
theta = np.zeros(2)
cost = computeCost(x, y, theta)
print("Lets see the initial cost: ", cost)

 # Some gradient descent settings
iterations = 1500;
alpha = 0.01;

#Gradient descent
theta = gradientDescent(x,y,theta,alpha,iterations)[0]

# Linear function with te new values of theta
fl = []
m = len(x)
for i in range(0,m):
    fl.append(theta[0] + x[i] * theta[1])

# Predict values for population sizes of 35,000 and 70,000
predict1 = theta[0]+theta[1] * 3.5
print("For population = 35,000, we predict a profit of: ", predict1 * 10000);
predict2 = theta[0]+theta[1] * 7
print("For population = 70,000, we predict a profit of: ",  predict2 * 10000);

# Plotting dataset and linear function
plt.axis([4, 24, -5, 25])
plt.ylabel('City Population')
plt.xlabel('Profit of Food Truck')
plt.plot(df["City Population"], df["Profit of Food Truck"], 'bo')
plt.plot(x, fl, 'r')
plt.show()