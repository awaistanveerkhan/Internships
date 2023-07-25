from flask import Flask, render_template, request
import joblib
import pandas as pd
import re
import numpy as np
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

app = Flask(__name__)

tokenizer_path = 'model/count_vectorizer.pkl'
model_path = 'model/pass_agg_model.pkl'
data_path = 'data/drugsComTrain_raw.csv'

vectorizer = joblib.load(tokenizer_path)
model = joblib.load(model_path)
dataset = pd.read_csv(data_path)

stop = stopwords.words('english')
lemmatizer = WordNetLemmatizer()


@app.route('/result',methods=["GET","POST"])
def predict():
	if request.method == 'POST':
		raw_text = request.form['rawtext']
		
		
		if raw_text != "":
			cleaned_text = clean_text(raw_text)
			clean_lst = [cleaned_text]
   
			vectors = vectorizer.transform(clean_lst)
			prediction = model.predict(vectors)
			predicted_cond = prediction[0]
			top_drugs = get_top_3_drugs(predicted_cond)
			
					
			return render_template('result.html',rawtext=raw_text,result=predicted_cond,top_drugs=top_drugs)
		else:
			 raw_text ="There is no text to select"



def clean_text(raw_review):
    review_text = BeautifulSoup(raw_review, 'html.parser').get_text()
    letters_only = re.sub('[^a-zA-Z]', ' ', review_text)
    words = letters_only.lower().split()
    meaningful_words = [w for w in words if not w in stop]
    lemmitize_words = [lemmatizer.lemmatize(w) for w in meaningful_words]
    return( ' '.join(lemmitize_words))

def get_top_3_drugs(diagnosed_disease):
    df_top = dataset[(dataset['rating']>=9)&(dataset['usefulCount']>=100)].sort_values(by = ['rating', 'usefulCount'], ascending = [False, False])
    drug_lst = df_top[df_top['condition']==diagnosed_disease]['drugName'].head(3).tolist()
    return drug_lst



@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
