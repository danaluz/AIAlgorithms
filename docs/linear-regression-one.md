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

#### [](#header-4) So..let's back to the code

The problem is:  _Suppose you are the CEO of a restaurant franchise and are considering diﬀerent cities for opening a new outlet. The chain already has trucks in various cities and you have data for proﬁts and populations from the cities. You would like to use this data to help you select which city to expand to next._

So, the idea is: given an X Population, how is the predicted profit?

Here is the general process:

![](https://www.lucidchart.com/publicSegments/view/2ee9f10a-5d8d-4453-8c2f-f029dd200341/image.jpeg)

We will try to undestand the data by plotting it:

![](http://lightgroup.com.ar/images_dana/Plotting_Data.PNG)




