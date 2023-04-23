import numpy as np
from array import *
import pandas as pd
from flask import Flask, request, jsonify, render_template, redirect, url_for
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from flask import send_from_directory
import pickle

app = Flask(__name__)

model = pickle.load(open("hack2.pkl", "rb"))


@app.route("/", methods=['POST', 'GET'])
def predict():
    # if request.method =="POST":

    return render_template("page1.html")


# @app.route("/predict", methods = ['POST'])
# def predict():
#     if request.method =="POST":
#         int_features = [int(x) for x in request.args.values()]
#         features = [np.array(int_features)]
#         # prediction = model.predict(features)
#         prediction=65
#         redirect(url_for('results',prediction=prediction))
#     # return render_template("project_hackathon.html",prediction_text = "the claim is: " .format(prediction))
#     return render_template('project_hackathon.html')

def convert_to_num(text):
    if text == "yes":
        return 1
    elif text == "no":
        return 2

@app.route('/results', methods=['POST', 'GET'])
def results():
    # value = request.args.get('prediction')
    text10=0
    OPAnnualReimbursementAmt = request.args.get('OPAnnualReimbursementAmt')
    OPAnnualDeductibleAmt = request.args.get('OPAnnualDeductibleAmt')
    DeductibleAmtPaid = request.args.get('DeductibleAmtPaid')
    period = request.args.get('period')
    phy_stats = request.args.get('phy_stats')
    print(type(phy_stats))
    claim_p = request.args.get('claim_p')
    RenalDiseaseIndicator = request.args.get('RenalDiseaseIndicator')
    age = request.args.get('age')
    Provider = request.args.get('Provider')
    NoOfMonths_PartACov = request.args.get('NoOfMonths_PartACov')
    NoOfMonths_PartBCov = request.args.get('NoOfMonths_PartBCov')
    ChronicCond_KidneyDisease = request.args.get('ChronicCond_KidneyDisease')
    # text = ChronicCond_KidneyDisease.replace('yes','2').replace('no','1')
    ChronicCond_Cancer = request.args.get('ChronicCond_Cancer')
    ChronicCond_ObstrPulmonary = request.args.get('ChronicCond_ObstrPulmonary')
    ChronicCond_Depression = request.args.get('ChronicCond_Depression')
    ChronicCond_Diabetes = request.args.get('ChronicCond_Diabetes')
    ChronicCond_IschemicHeart = request.args.get('ChronicCond_IschemicHeart')
    ChronicCond_stroke = request.args.get('ChronicCond_stroke')
    ChronicCond_Alzheimer = request.args.get('ChronicCond_Alzheimer')
    # ClaimID = request.args.get('ClaimID')
    # @app.route('/access-array')
    # def replace():
    #     columns = ['ChronicCond_Alzheimer', 'ChronicCond_KidneyDisease', 'ChronicCond_Cancer', 'ChronicCond_ObstrPulmonary', 'ChronicCond_Depression', 'ChronicCond_Diabetes', 'ChronicCond_IschemicHeart', 'ChronicCond_stroke']
    #     columns_element = []
    #     for element in columns:
    #         if columns(element) == "yes":
    #             text = 1
    #         elif columns(element) == "no":
    #             text = 2
    #         columns(element) = text
    ChronicCond_KidneyDisease = convert_to_num(ChronicCond_KidneyDisease)
    print(ChronicCond_KidneyDisease)
    # if ChronicCond_stroke == "yes":
    #     text2 = 1
    # elif ChronicCond_stroke == "no":
    #     text2 = 2
    # ChronicCond_stroke = text2
    # if ChronicCond_Diabetes == "yes":
    #     text3 = 1
    # elif ChronicCond_Diabetes == "no":
    #     text3 = 2
    # ChronicCond_stroke = text3
    # if ChronicCond_IschemicHeart == "yes":
    #     text4 = 1
    # elif ChronicCond_IschemicHeart == "no":
    #     text4 = 2
    # ChronicCond_IschemicHeart = text4
    # if ChronicCond_Cancer == "yes":
    #     text5 = 1
    # elif ChronicCond_Cancer == "no":
    #     text5 = 2
    # ChronicCond_Cancer = text5
    # if ChronicCond_Depression == "yes":
    #     text6 = 1
    # elif ChronicCond_Depression == "no":
    #     text6 = 2
    # ChronicCond_Depression = text6
    # if ChronicCond_ObstrPulmonary == "yes":
    #     text7 = 1
    # elif ChronicCond_ObstrPulmonary == "no":
    #     text7 = 2
    # ChronicCond_ObstrPulmonary = text7
    # if ChronicCond_Alzheimer == "yes":
    #     text8 = 1
    # elif ChronicCond_Alzheimer == "no":
    #     text8 = 2
    print(text10)
    if phy_stats == "all same":
        text10 = 3
    elif phy_stats == "two same":
        text10 = 2
    elif phy_stats == "none same":
        text10 = 1
    print(text10)
    phy_stats = text10
    int_features = []
    for x in request.args.values():
        # x = request.args.values()[i]

        if x == "yes":
            x = 1
        elif x == "no":
            x=2
        # else:
        #     return 'Invalid input, please enter "yes" or "no".'
        int_features.append(x)
    print(int_features)

    # int_features = [float(x) for x in request.args.values()]
    features = [np.array(int_features)]
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(features)
    prediction = model.predict(scaled_data)
    # return redirect(url_for('results', prediction=0))
    #
    # print(value)
    # pred = model.predict(value)

    return render_template('results.html', value=prediction)

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('static', path)

@app.route("/index")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False, port=5000)
