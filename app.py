from flask import Flask,render_template,request
import numpy as np
import sklearn
import pickle
import joblib

app=Flask(__name__)
model=joblib.load('model.pkl')
f_final=list()
s=list()
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result=request.form['Years of Experience']
        s.insert(1,int(result))
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        #pickled_model = joblib.load('model.pkl')
        f=[]
        f=model.predict(final_features)
        f_final.insert(int(result),f)
        n=tuple(f_final)
    return render_template("index.html", result=n,s=s)
@app.route("/home")
def root():
    a=[]
    for x in range(1,4):
        a=x
    return render_template("index.html",content=["Vincent","victor"])
if __name__=="__main__":
    app.run(debug=True)
