# NYC-Subway

# Section 0. References

## 0.1 Welch T Test
- Intro to Data Science course at Udacity
- http://stackoverflow.com/questions/22611446/perform-2-sample-t-test
- http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.stats.ttest_ind.html

## 0.2 Mann Whitney Test


# Section 1. Statistical Test


1.1 Which statistical test did you use to analyze the NYC subway data? Did you use a one-tail or a two-tail P value? What is the null hypothesis? What is your p-critical value?
```
a) Mann Withney test is used to analyze NYC subway data.
b) A one tail P value is used as we want to know if NYC subway ridership is greater given rainy days.
c) The null hypothesis is: Ho: P(ridership|no-rain > ridership|rain) >=  0.5
   The alterntaive hypothesis is: H1: P(ridership|no-rain > ridership|rain) <  0.5
d) The chosen p-critical value is 0.05.
```


1.2 Why is this statistical test applicable to the dataset? In particular, consider the assumptions that the test is making about the distribution of ridership in the two samples.
```
Mann Whitney test makes the assumption of independent samples (with no overlap in ridership).  Also there are far more samples than 20 in the dataset and a priori both distributions are unknown.  Therefore the statistical test can be applied.
```

1.3 What results did you get from this statistical test? These should include the following numerical values: p-values, as well as the means for each of the two samples under test.
```
Hourly entries with rain:    mean = 1105.45, variance = 2.47832e+11
Hourly entries without rain: mean = 1090.28, variance = 4.72824e+11
Mann Whitney test: U = 1.92441e+09, p = 0.0193096
```

1.4 What is the significance and interpretation of these results?
```
With Mann Whitney test p = 0.01936 < 0.05 => Null hypothesis is rejected.  We can state that on rainy days there is more ridership at the NYC subway.
```


# Section 2. Linear Regression

2.1 What approach did you use to compute the coefficients theta and produce prediction for ENTRIESn_hourly in your regression model:

    OLS using Statsmodels or Scikit Learn
    Gradient descent using Scikit Learn
    Or something different?
```
I used an OLS approach for computing coeficients and produce a prediction.
```

2.2 What features (input variables) did you use in your model? Did you use any dummy variables as part of your features?
```
I used 'meanwindspdi','meantempi','precipi','rain', 'Hour','maxtempi' and UNIT as dummy variable.
```
2.3 Why did you select these features in your model? We are looking for specific reasons that lead you to believe that

the selected features will contribute to the predictive power of your model.

    Your reasons might be based on intuition. For example, response for fog might be: “I decided to use fog because I thought that when it is very foggy outside people might decide to use the subway more often.”
    Your reasons might also be based on data exploration and experimentation, for example: “I used feature X because as soon as I included it in my model, it drastically improved my R2 value.”  

```
At first I thought that meteorological magnitudes linked with rain would improve the prediction, such as minpressure, mindewpti, precipi, fog and thunder.  After doing some experimentation I found out that thunder wasn´t useful.  I also experimented by adding all variables and testing each time with one less as far as I saw that my R^2 didn´t improve.
```

2.4 What are the parameters (also known as "coefficients" or "weights") of the non-dummy features in your linear regression model?
```
intercept         992.499526
meanwindspdi      21.398801
meantempi        -29.920590
precipi           32.292600
rain              22.553125
Hour              67.418064
maxtempi          23.017546
```

2.5 What is your model’s R2 (coefficients of determination) value?
```
R^2 coefficient = 0.458889
```

2.6 What does this R2 value mean for the goodness of fit for your regression model? Do you think this linear model to predict ridership is appropriate for this dataset, given this R2  value?
```
The previous value is a low value, saying that my regression model does not fit well the given data.  This means that it is not a good model to use for prediction.  This means that the ratio of residual variability is high and the model only explains a 46% of the original variability. Finally R is a masurement of how well predictors are related with the independent variable.
```

# Section 3. Visualization

3.1 Visualization of ENTRIESn_hourly for rainy days and one of ENTRIESn_hourly for non-rainy days.
![alt text](https://cloud.githubusercontent.com/assets/7275475/12863478/e100dab4-cc76-11e5-9efd-ea802f0cd9f4.png "NYC_Ridership_Histogram")

3.2 One visualization can be more freeform. You should feel free to implement something that we discussed in class (e.g., scatter plots, line plots) or attempt to implement something more advanced if you'd like.
![alt text](https://cloud.githubusercontent.com/assets/7275475/12863551/a7c477e6-cc77-11e5-8eef-c0901f1127ef.png)

![alt text](https://cloud.githubusercontent.com/assets/7275475/12863553/aba5525e-cc77-11e5-8bab-1ec20a819c43.png)

![alt text](https://cloud.githubusercontent.com/assets/7275475/12863555/ae45c4da-cc77-11e5-9acc-753f0a91b51f.png)


# Section 4. Conclusion

4.1 From your analysis and interpretation of the data, do more people ride the NYC subway when it is raining or when it is not raining?
```
If we look barely to the histogram of 3.1 we could wrongly say that there is more ridership at days without rain than at days with rain.  But this is not true as Mann Whitney test results show.  With Mann Whitney test p = 0.01936 < 0.05 => Null hypothesis is rejected.  We can state that on rainy days there is more ridership at the NYC subway.
```

4.2 What analyses lead you to this conclusion? You should use results from both your statistical tests and your linear regression to support your analysis.
```
As said before, after running the Mann Whitney test p = 0.01936 < 0.05 => Null hypothesis is rejected.  We can state that on rainy days there is more ridership at the NYC subway.

If we look at the regression parameters we can appreciate that meteorological variables usually associated with rain have positive values, including the variable rain itself.  This points out what the Mann Whitney test stated.

meanwindspdi      21.398801
meantempi        -29.920590
precipi           32.292600
rain              22.553125
Hour              67.418064
maxtempi          23.017546
```

# Section 5. Reflection
5.1 Please discuss potential shortcomings of the methods of your analysis, including dataset and analysis, such as the linear regression model or statistical test.
```
Regarding the dataset it appears to be some kind of sample measurement frequency for each line, which can miss some type of trend that should be studied. At the regression model the dummy units variable parameters have very high values to those of the none dummy variables.  This translates to a strong dependecny on unit lines.  Also if instead of a p-critical value of 0.05 we had chosen 0.01, we could not have rejected the null hypothesis.
```
