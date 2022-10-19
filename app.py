from flask import Flask,render_template,url_for,request, jsonify
import numpy as np
import pickle5 as pickle
import pandas as pd
from keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import model_from_json
from numpy import array
import sqlite3

app=Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("Drug-Review-Sentiment-Analysis-RNN-Bidirectional-lstm--Flask-Deployment-master\database.db")
    except sqlite3.error as e:
        print(e)
    return conn

model = load_model(r"Drug-Review-Sentiment-Analysis-RNN-Bidirectional-lstm--Flask-Deployment-master\rnn_model.h5")


with open(r'Drug-Review-Sentiment-Analysis-RNN-Bidirectional-lstm--Flask-Deployment-master\tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST', 'GET'])
def predict():
    
    max_length = 200
    if request.method == 'POST':
        review = request.form['review']
        data = [review]
        tokenizer.fit_on_texts(data)
        enc = tokenizer.texts_to_sequences(data)
        enc=pad_sequences(enc, maxlen=max_length, padding='post')
        my_prediction = model.predict(array([enc][0]))[0][0]
        class1 = model.predict_classes(array([enc][0]))[0][0]
        print(class1)

    
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "POST":
        new_text = request.form["review"]
        sql = """INSERT INTO reviews (review)
                 VALUES (?)"""
        cursor = cursor.execute(sql, (new_text,))
        conn.commit()

    if class1 == 1:
        good = True
    else:
        good = False

    if class1 == 0:
        bad = True
    else:
        bad = False
    
   
    if request.method == "POST":
        p_sentiment = good
        n_sentiment = bad
        sql_two = """INSERT INTO sentiments (positive, negative)
                 VALUES (?, ?)"""
        cursor = cursor.execute(sql_two, (p_sentiment, n_sentiment))
        conn.commit()

    # if request.method == "GET":
    #     cursor = conn.execute("SELECT * FROM database")
    #     database = [
    #         dict(id=row[0], reviews=row[1], sentiment=row[2])
    #         for row in cursor.fetchall()
    #     ]
    #     if database is not None:
    #         return jsonify(database)
       
    return render_template('result.html',prediction = class1)



if __name__ == '__main__':
    app.run(debug=True)
    