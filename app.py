#!/c/users/bhavy/anaconda3/lib
import numpy as np
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    '''features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)'''
    weight = float(request.form['Item_Weight'])
    
    if(request.form['Item_Fat_Content'] == 'Low Fat'):
        fat = 0
    elif(request.form['Item_Fat_Content'] == 'Regular'):
        fat = 2
    else:
        fat = 1
    visible = float(request.form['Item_Visibility'])
    Itype = int(request.form['Item_Type'])
    mrp = float(request.form['Item_MRP'])
    identifier = int(request.form['Outlet_Identifier'])
    year = int(request.form['Outlet_Establishment_Year'])
    if(request.form['Outlet_Size'] == 'High'):
        size = 0
    elif(request.form['Outlet_Size'] == 'Small'):
        size = 2
    else:
        size = 1
    if(request.form['Outlet_Location_Type'] == 'Tier 1'):
        location = 0
    elif(request.form['Outlet_Location_Type'] == 'Tier 3'):
        location = 2
    else:
        location = 1
    if(request.form['Outlet_Type'] == 'Grocery Store'):
        Otype = 0
    elif(request.form['Outlet_Type'] == 'Supermarket Type1'):
        Otype = 1
    elif(request.form['Outlet_Type'] == 'Supermarket Type2'):
        Otype = 2
    else:
        Otype = 3
    if(request.form['New_Item_Type'] == 'Drinks'):
        Ntype = 0
    elif(request.form['New_Item_Type'] == 'Non-consumable'):
        Ntype = 2
    else:
        Ntype = 1
    features = [weight,fat,visible,Itype,mrp,identifier,year,size,location,Otype,Ntype]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 5)
    final_output = round((np.exp(output)-1),2);
    
    return render_template('index.html', prediction_text='Prediction Sales should be  {}'.format(final_output))



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, use_reloader=False)