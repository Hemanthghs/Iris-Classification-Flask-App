from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("iris_model.sav")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def result():
    s_length = float(request.form['sepal_length'])
    s_width = float(request.form['sepal_width'])
    p_length = float(request.form['petal_length'])
    p_width = float(request.form['petal_width'])
    
    pred = model.predict([[s_length, s_width, p_length, p_width]])
    
    
    return render_template("index.html", result = pred[0])
   
    
    
    

if __name__ == '__main__':
    app.run()