


from flask import Flask,render_template,request
import pickle

app=Flask(__name__)

patient  = pickle.load(open('D:\Machine_Learning _Algorithms\ML_PROJECT\Dibetes\model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods= ["GET","POST"])
def student():

    var_Pregnancies= int(request.form.get('Pregnancies'))
    var_Glucose= int(request.form.get('Glucose'))
    var_BloodPressure= int(request.form.get('BloodPressure'))
    var_SkinThickness= int(request.form.get('SkinThickness'))
    var_Insulin= int(request.form.get('Insulin'))
    var_BMI= float(request.form.get('BMI'))
    var_DiabetesPedigreeFunction= float(request.form.get('DiabetesPedigreeFunction'))
    var_Age= int(request.form.get('Age'))

    
    
    
    
    result =patient.predict([[var_Pregnancies,var_Glucose,var_BloodPressure,var_SkinThickness,var_Insulin,var_BMI,var_DiabetesPedigreeFunction,var_Age]])
    print(result[0])
    

    if result[0] == 1:
        return "Dibeties Positive"

    else:
        return "not positive"

if __name__ =='__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)



