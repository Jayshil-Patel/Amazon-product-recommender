from flask import Flask, request,jsonify
import numpy as np
import pandas as pd
import json
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World. I am Jayshil. Welcome to the session!'

df = pd.read_csv('amazon.csv')
df = pd.read_csv('amazon.csv')
df = df.drop(['review_id', 'review_title', 'review_content', 'img_link','user_name','discounted_price','actual_price','discount_percentage'], axis=1) 
df = df.drop_duplicates()
df = df.dropna()
label_encoder = LabelEncoder()
df['category'] = label_encoder.fit_transform(df['category'])
df['product_id'] = label_encoder.fit_transform(df['product_id'])
df['product_name'] = df['product_name'].str.lower().replace('[^\w\s]','').str.strip()
vectorizer = TfidfVectorizer()
product_vectors = vectorizer.fit_transform(df['product_name'])
response={}

@app.route('/recommend', methods=['POST'])
def recommend():
    global input_product_name
    if request.json['queryResult']['intent']['displayName'] == "product_identifier":
        input_product_name = request.json['queryResult']['parameters']['product']    
        input_product_name = input_product_name.lower().replace('[^\w\s]','').strip()
        input_product_vector = vectorizer.transform([input_product_name])
        similarities = cosine_similarity(input_product_vector, product_vectors).flatten()
        similar_products_indices = similarities.argsort()[::-1][:5]
        similar_products = df.iloc[similar_products_indices]['product_name']
        stri = ""
        similar_products_list = similar_products.tolist()
        stri = stri + similar_products_list[0]
        response = {
            "fulfillmentText": f"we recommend you \n'{stri}'"
        } 
    else:
        # input_product_name = request.json['queryResult']['parameters']['product']    
        input_product_name = input_product_name.lower().replace('[^\w\s]','').strip()
        input_product_vector = vectorizer.transform([input_product_name])
        similarities = cosine_similarity(input_product_vector, product_vectors).flatten()
        similar_products_indices = similarities.argsort()[::-1][:5]
        similar_products = df.iloc[similar_products_indices]['product_name']
        stri = ""
        similar_products_list = similar_products.tolist()
        stri = stri + similar_products_list[0]
            
        product_name = similar_products_list[0]
        filtered_df = df[df['product_name'] == product_name]
        product_link = filtered_df['product_link'].iloc[0]
        response = {
            "fulfillmentText": f"Here is the link \n'{product_link}'"
        }

   
    return response


if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))
