from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':


        # Code changes only from here

        Longitude =  request.form['Longitude']
        Latitude =  request.form['Latitude']
        Median_Age_of_Household = request.form['Median_Age_of_Household']
        Total_Rooms = request.form['Total_Rooms']
        Total_Bedrooms = request.form['Total_Bedrooms']
        Population = request.form['Population']
        Households = request.form['Households']
        Median_Income = request.form['Median_Income']
        ONE_H_OCEAN = request.form['ONE_H_OCEAN']
        INLAND = request.form['INLAND']
        NEAR_BAY = request.form['NEAR_BAY']
        NEAR_OCEAN = request.form['NEAR_OCEAN']

        data = [[float(Longitude),float(Latitude),float(Median_Age_of_Household),float(Total_Rooms),float(Total_Bedrooms),
        float(Population),float(Households),float(Median_Income),float(ONE_H_OCEAN),float(INLAND),float(NEAR_BAY),float(NEAR_OCEAN)]]
        model = pickle.load(open('data.pkl','rb'))
        prediction = model.predict(data)[0]

        # Code modifications upto here



        return render_template('index.html',prediction = prediction)

 
if __name__ == "__main__":
    app.run()

