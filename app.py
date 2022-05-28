import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')  
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    horsepower=int(request.form['horsepower'])
    curb_weight=int(request.form['curb-weight'])
    engine_size=int(request.form['engine-size'])
    highway_mpg=int(request.form['highway-mpg'])
    bore=float(request.form['bore'])
    wheel_base=float(request.form['wheel-base'])
    city_mpg=int(request.form['city-mpg'])
    length=float(request.form['length'])
    width=float(request.form['width'])
    prediction=model.predict([[horsepower,curb_weight,engine_size,highway_mpg,bore,wheel_base,city_mpg,length,width]])
    output = round(prediction[0],2)
    return render_template('index.html',prediction_text="PRICE OF THE VEHICLE IS Rs.{}".format(output))   

if __name__ == '__main__':
    app.run(debug=True)    