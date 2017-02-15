### [](#header-3) Linear Regression with One Variable

#### [](#header-4) Getting started: the Anscombe's quartet

In 1973, Anscombe published this [paper](http://www.sjsu.edu/faculty/gerstman/StatPrimer/anscombe1973.pdf) showing how important is to graph the data whenever possible. Anscombe create four small datasets really different between each other. 
But it turns out, all the four has the same linear regression coeficient (as you can see on the red line).

![](http://lightgroup.com.ar/images_dana/anscombe.png)

Furthermore, if we compute the means, the variance and the correlation, all four give us the same values:

| Graph        | Mean X  | Variance X | Mean Y | Corr(x,y) |
|:-------------|:--------|:-----------|:-------|:----------|
| Linear       | 9       | 11         | 7.5    | 0.816     |
| Polynomial   | 9       | 11         | 7.5    | 0.816     |
| Outlier X    | 9       | 11         | 7.5    | 0.816     |
| Outlier Y    | 9       | 11         | 7.5    | 0.816     |


With this in mind, the first thing to do, is trying to plot the dataset so we can get a glimpse of the data.

#### [](#header-4) Let's back to the code

I was doing the Coursera course on [Machine Learning](https://www.coursera.org/learn/machine-learning) and I thought that it'll nice to try out and coded the weekly exercise on a different lenguage, and [we the previous experience on Python](k-nn-v1.md), why not give it a shot?

The problem is:  _Suppose you are the CEO of a restaurant franchise and are considering diﬀerent cities for opening a new outlet. The chain already has trucks in various cities and you have data for proﬁts and populations from the cities. You would like to use this data to help you select which city to expand to next._

The idea is: **given an X Population, how much is the predicted profit?**

We will try to undestand a little bit of the data by plotting it:


```python
import matplotlib.pyplot as plt
import pandas

with open("ex1data1.txt", 'r') as csvfile:
    ex1 = pandas.read_csv(csvfile)
    
df = pandas.DataFrame(ex1)

x = df["City Population"].as_matrix()
y = df["Profit of Food Truck"].as_matrix()

plt.axis([4, 24, -5, 25])
plt.ylabel('City Population')
plt.xlabel('Profit of Food Truck')
plt.plot(x, y, 'bo')
plt.show()
```

And this is our first result:

![](http://lightgroup.com.ar/images_dana/Plotting_Data.PNG)

We have to find the coefficients of a linear function y = **theta 1**x + **theta 0** that better fit the given data.  The general process on this algorithm consist on **obtain the theta values that minimize the cost**:
![](http://lightgroup.com.ar/images_dana/costFunction.PNG)

```python
def computeCost(X, y, theta):
    m = len(y)
    n=0.0
    for i in range(0,m):
        n += (theta[0]+ theta[1]*X[i] - y[i]) ** 2
        print(n)
    J = (1 / (2 * m)) * n
    return J;
```

And this can be done through a gradient function:

```python
def gradientDescent(X, y, theta, alpha, num_iters):
    m = len(y)
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

    return theta;
```

This is how my code is structured:

   ![](https://www.lucidchart.com/publicSegments/view/2ee9f10a-5d8d-4453-8c2f-f029dd200341/image.jpeg)


And this is the final plot:
![](http://lightgroup.com.ar/images_dana/Plotting_Data_LR.PNG)
Of course, this is just an overview, and I strongly recommend to take the course. 


