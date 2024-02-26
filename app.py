from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from LifeExpentancyProject.pipeline.prediction import PredictionPipeline


app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 


@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            Country = request.form.get('Country')
            Year = int(request.form.get('Year'))
            Status = float(request.form.get('Status'))
            Adult_Mortality = float(request.form.get('Adult Mortality') or 0)  # Handle None
            infant_deaths = int(request.form.get('infant deaths') or 0)  # Handle None
            Alcohol = float(request.form.get('Alcohol') or 0)  # Handle None
            percentage_expenditure = float(request.form.get('percentage expenditure') or 0)  # Handle None
            Hepatitis_B = float(request.form.get('Hepatitis B') or 0)  # Handle None
            Measles = int(request.form.get('Measles') or 0)  # Handle None
            BMI = float(request.form.get('BMI') or 0)  # Handle None
            under_five_deaths = int(request.form.get('under-five deaths') or 0)  # Handle None
            Polio = float(request.form.get('Polio') or 0)  # Handle None
            Total_expenditure = float(request.form.get('Total expenditure') or 0)  # Handle None
            Diphtheria = float(request.form.get('Diphtheria') or 0)  # Handle None
            HIV_AIDS = float(request.form.get('HIV/AIDS') or 0)  # Handle None
            GDP = float(request.form.get('GDP') or 0)  # Handle None
            Population = float(request.form.get('Population') or 0)  # Handle None
            thinness = float(request.form.get('thinness') or 0)  # Handle None
            thinness_5_9_years = float(request.form.get('thinness 5-9 years') or 0)  # Handle None
            Income_composition_of_resources = float(request.form.get('Income composition of resources') or 0)  # Handle None
            Schooling = float(request.form.get('Schooling') or 0)  # Handle None
         
            data = [Country,Year,Status,Adult_Mortality,infant_deaths,Alcohol,percentage_expenditure,
                    Hepatitis_B,Measles,BMI,under_five_deaths,Polio,Total_expenditure,Diphtheria,HIV_AIDS,
                    GDP, Population,thinness,thinness_5_9_years,Income_composition_of_resources,Schooling]
            data = np.array(data).reshape(1, 21)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = round(predict[0]))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080, debug=True)
	# app.run(host="0.0.0.0", port = 8080)