import pandas as pd 
import numpy as np 
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.linear_model.logistic import  LogisticRegression  
from sklearn.model_selection import train_test_split, cross_val_score 
  
# read files and reformat
df = pd.read_csv('./SMSSpamCollection', delimiter='\t', header=None)  
  
# split data into 2/3 of training data and 1/3 of test data
X_train_raw, X_test_raw, y_train, y_test = train_test_split(df[1],df[0], test_size=0.33) 
  
# extract feature using TF-IDF
# get more information here: https://nlp.stanford.edu/IR-book/html/htmledition/tf-idf-weighting-1.html
vectorizer = TfidfVectorizer()  
X_train = vectorizer.fit_transform(X_train_raw)  
X_test = vectorizer.transform(X_test_raw)  
  
# use logistic regression to train model and predict test data  
classifer = LogisticRegression()  
classifer.fit(X_train,y_train)  
predictions = classifer.predict(X_test)  
 
# accuracy
nErrors = (y_test != predictions).sum()
accuracy = 1.0 - nErrors / y_test.shape[0]
print("Accuracy: ", accuracy)

# sample test data
mess = ['you are a WINNER!! To claim 1000$ call 99999999', "I am ready to invest in dating service"]
output = classifier.predict(vectorizer.transform(mess))

for i ,m in enumerate(mess):
	print m, ' == ', output[i]
