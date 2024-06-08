from flask import Flask, render_template, redirect, url_for, request
from form import input
import joblib
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'aetege'

model = joblib.load('iris.joblib')

@app.route('/',methods=['GET', "POST"])
def home():
    fo  = input()
    if fo.validate_on_submit():
        x_new = pd.DataFrame(dict(
            sepal_length=[fo.sl.data],
            sepal_width=[fo.sw.data],
            petal_length=[fo.pl.data],
            petal_width=[fo.pw.data]  ))
        pred = model.predict(x_new)[0]
        output = f'The predicted Species is {pred}'
        return render_template('pred.html', form=fo, out=output, show_result=True)
    else:
        output = 'Please give details to predict'
        return render_template('pred.html', form=fo, out=output, show_result=True)
    
    


if __name__ == '__main__':
    app.run(debug=True)