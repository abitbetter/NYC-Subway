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
a) Welch T test and Mann Withney test are used.
b) A one tail P value is used as we want to know if NYC subway ridership is greater given rainy days.
c) The null hypothesis is: Ho: u-rain <=  u-no-rain
   The alterntaive hypothesis is: H1: u-rain > u-no-rain
d) The chosen p-critical value is 0.05.
```


1.2 Why is this statistical test applicable to the dataset? In particular, consider the assumptions that the test is making about the distribution of ridership in the two samples.
```
Both Welch T test and Mann Whitney test make the assumption of independent samples (with no overlap in ridership).  Also in this dataset the two samples have unequal variances and unequal sample sizes.  Therefore both statistical tests can be applied.
```

1.3 What results did you get from this statistical test? These should include the following numerical values: p-values, as well as the means for each of the two samples under test.
```
Hourly entries with rain:    mean = 1105.45, variance = 2.47832e+11
Hourly entries without rain: mean = 1090.28, variance = 4.72824e+11
Welch T test: t = 1.10421, two-tail p = 0.269506, one-tail p = 0.134753
Mann Whitney test: U = 1.92441e+09, p = 0.0193096
```

1.4 What is the significance and interpretation of these results?
```
With Welch T test p = 0.134753 > 0.05 => Null hypothesis is not rejected.  We cannot state that both samples have different mean.
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
I used 'maxdewpti','minpressurei','fog','rain','mintempi','meantempi' and UNIT as dummy variable.
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
intercept        11712.977809
maxdewpti          19.467820
minpressurei     -320.859344
fog                46.255463
rain             -133.283497
mintempi          -56.167069
meantempi          23.311473
```

2.5 What is your model’s R2 (coefficients of determination) value?
```
R^2 coefficient = 0.420821
```

2.6 What does this R2 value mean for the goodness of fit for your regression model? Do you think this linear model to predict ridership is appropriate for this dataset, given this R2  value?
```
The previous value is a low value, saying that my regression model does not fit well the given data.  This means that it is not a good model to use for prediction.
```
