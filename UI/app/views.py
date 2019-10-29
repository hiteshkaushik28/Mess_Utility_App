import sys
from pathlib import Path
from app import app
from flask import Flask,render_template,request,redirect
import numpy as np
from openpyxl import load_workbook
import json

wb = load_workbook(filename = 'food_labelling.xlsx')
mon = wb['Mon']
# print(mon['A23'].value)
# print(wb['Mon']['A1'].value)

@app.route('/')
def firstpage():
    return render_template('index.html')

@app.route('/preferences/', methods = ['GET','POST'])
def fetch_data():
    # if request.method == "GET":
    #     day = request.args.get('day')
    #     meal = request.args.get('meal')
    print("hello")
    return render_template('preferences.html')
    # return render_template('preferences.html', day = day, meal = meal)
    # return(json.dumps(""))
