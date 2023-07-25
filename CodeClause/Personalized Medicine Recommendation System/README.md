# Medical Condition Predictor & Drug Recommendation System
This Flask Web Based Natural Language Processing project on Medical Condition Prediction & Drug Recommendation System is a part of remote internship as a Data Scientist at CodeClause! 

You can get the dataset from [here](https://archive.ics.uci.edu/ml/datasets/Drug+Review+Dataset+%28Drugs.com%29) and complete video explanation from [here](https://drive.google.com/drive/folders/1mZPfl1JEezIDOmo8Q9V7xn4yBkk7LUD0?usp=drive_link).

## Dataset Information
The dataset contains 161k reviews along with ratings of different users who have used different medicinces for different diseases. For training & model, I have worked on just 4 diseases:
<br>1. Depression
<br>2. Birth Control
<br>3. Diabetes, Type 2
<br>4. High Blood Pressure

## Project Information
For sentiment analysis, I worked on `Reviews` & `Conditions` using `Bag of Words` model. For model training, I tested `MultinomialNB` & `PassiveAggressiveClassifier` which both achieved tremendous accuracy of 97% & 98% respectively.

After classification of disease, I fetched the Top 3 drugs on the criteria of `Drugs having rating above 9 and usefulCount of above 100`

For deploying my model on Flask Web App, I used joblib `dump` & `load` functions to save and load my model respectively.