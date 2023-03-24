from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
scaler=pickle.load(open('scale.pkl','rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def predict():
    data=[float(x) for x in request.form.values()]
    scale_data=scaler.transform([data])
    result=model.predict(scale_data)

    final_result=result[0]
    
    if final_result=="M":
        return "<h1 style='color:green'>The Female is Suffering From = Malignant Type of Breast Cancer</h1>"
        
    else:
        return "<h1 style='color:red'>The Female is Suffering From = Benign Type of Breast Cancer</h1>"



