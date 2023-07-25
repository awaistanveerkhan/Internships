# Wine Quality Prediction
This Machine Learning project on Wine Quality Prediction is a part of remote internship as a Data Scientist at CodeClause!

## Dataset Information
The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are munch more normal wines than excellent or poor ones). Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods. Two datasets were combined and few values were randomly removed.

### Attribute Information:
Input variables (based on physicochemical tests):<br>
1 - fixed acidity<br>
2 - volatile acidity<br>
3 - citric acid<br>
4 - residual sugar<br>
5 - chlorides<br>
6 - free sulfur dioxide<br>
7 - total sulfur dioxide<br>
8 - density<br>
9 - pH<br>
10 - sulphates<br>
11 - alcohol<br>
Output variable (based on sensory data):<br>
12 - quality (score between 3 and 9)

### Project Information:
The project focused on leveraging machine learning algorithms to predict the quality of wines based on various features, such as `acidity`, `pH levels`, `residual sugar`, and more. To accomplish this, I employed different machine learning algorithms, including `decision trees`, `random forests`, `extra trees classifier`, and `LGBM classifier`, to train and evaluate predictive models. The `extra trees classifier model` achieved an impressive accuracy rate of `89%` and a cross-validation score of `83%`. The project contains `box plots`,`histograms` etc to analyze plots and draw insights from them.
