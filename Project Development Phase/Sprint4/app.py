import requests

import flask
from flask import request, render_template
from flask_cors import CORS
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "5BR0_y5fBo2IbTXwV9OPjpyXJddc-hVoizqrBZOo3Uxh"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


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
   
    payload_scoring = {"input_data": [{"field": [['input1','input2','input3','input4','input5','input6','input7','input8','input9','input10']], "values": X}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/98b8a604-b27a-4f5d-a7cc-ee8c7a680d49/predictions?version=2022-11-15', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
    print(response_scoring)
    predictions = response_scoring.json()
    predict = predictions['predictions'][0]['values'][0][0]
    print("Final prediction :",predict)
    
    # showing the prediction results in a UI# showing the prediction results in a UI
    return render_template('predict.html',predict=("{:.2f} Lakhs".format(predict)))

if __name__ == '__main__' :
    app.run(debug= False)

