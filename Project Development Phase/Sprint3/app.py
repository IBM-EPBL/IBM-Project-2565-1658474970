import flask
from flask import request, render_template
from flask_cors import CORS
import joblib
 
app = flask.Flask(__name__, static_url_path='')
CORS(app)
 
@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index.html')
 
@app.route('/predict', methods=['POST'])
def predictprice():
	input1 = int(12)#(request.form['input1'])
	input2 = int(request.form['input2'])
	input3 = int(request.form['input3'])
	input4 = int(request.form['input4'])
	input5 = int(request.form['input5'])
	input6 = int(request.form['input6'])
	input7 = int(request.form['input7'])
	input8 = int(request.form['input8'])
	input9 = int(request.form['input9'])
	input10 = int(request.form['input10'])
	X = [[input1,input2,input3,input4,input5,input6,input7,input8,input9,input10]]
	model = joblib.load('predict_model.pkl')
	price = model.predict(X)[0]
	return render_template('predict.html',predict=("{:.2f} Lakhs".format(price)))
 
if __name__ == '__main__':
    app.run()


