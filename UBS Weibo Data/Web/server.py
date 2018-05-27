#import essential libraries
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import json
import re 
#from pymongo import MongoClient



#create an instance of Flask class
tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


# use this part to enable mongo db connection 
#client = MongoClient("mongodb://localhost:27017")
#db = client['fyp']





@app.route("/")
def homePage():
	return render_template('homePage.html')


@app.route("/ranking")
def showCluster():
	return render_template('Ranking.html')

@app.route("/bubbleStock")
def showBubbleStock():
	return render_template('bubbleStock.html')

@app.route("/bubbleChineseArt")
def showBubbleCA():
	return render_template('bubbleChineseArt.html')

@app.route("/bubbleGolf")
def showBubbleGolf():
	return render_template('bubbleGolf.html')

@app.route("/bubbleOverseasEducation")
def showBubbleOE():
	return render_template('bubbleOverseasEducation.html')


 
 
if __name__ == "__main__":
    app.run()
