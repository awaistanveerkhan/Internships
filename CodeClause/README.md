# CodeClause Data Science Internship Program

## Task1 - Wine Quality Prediction
The project focused on leveraging machine learning algorithms to predict the quality of wines based on various features, such as `acidity`, `pH levels`, `residual sugar`, and more. To accomplish this, I employed different machine learning algorithms, including `decision trees`, `random forests`, `extra trees classifier`, and `LGBM classifier`, to train and evaluate predictive models. The `extra trees classifier model` achieved an impressive accuracy rate of `89%` and a cross-validation score of `83%`. The project contains `box plots`,`histograms` etc to analyze plots and draw insights from them.<br>

## Task2 - Apple Stock Prediction & Forecasting
I implemented a `Stacked LSTM` architecture, a powerful variant of `recurrent neural networks` (RNNs), to capture the temporal dependencies in the stock data. By stacking `multiple LSTM layers`, I aimed to enhance the model's ability to learn complex patterns and make accurate predictions. The model trained at an incredibly lower loss and validation loss. During the project, I focused on utilizing the `closing stock` prices of Apple on a daily basis, and later `forecasted` the next `30 days` closing stock prices of Apple. <br>

## Task3 - Flask Web Based Personalized Medicince Recommendation System
The dataset contains 161k reviews along with ratings of different users who have used different medicinces for different diseases. For training & model, I have worked on just 4 diseases:
<br>1. Depression
<br>2. Birth Control
<br>3. Diabetes, Type 2
<br>4. High Blood Pressure<br>

For sentiment analysis, I worked on `Reviews` & `Conditions` using `Bag of Words` model. For model training, I tested `MultinomialNB` & `PassiveAggressiveClassifier` which both achieved tremendous accuracy of 97% & 98% respectively. After classification of disease, I fetched the Top 3 drugs on the criteria of `Drugs having rating above 9 and usefulCount of above 100`
For deploying my model on Flask Web App, I used joblib `dump` & `load` functions to save and load my model respectively.