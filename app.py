from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn

model = pickle.load(open('RandomForest1.pkl','rb'))

app = Flask(__name__)

# # Pass the required route to the decorator.
@app.route('/',methods=['GET','POST'])
def index():
    return render_template ('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST' :

        # Customer_Age
        Customer_Age = float(request.form['Customer_Age'])


        # Gender
        Gender = request.form["Gender"]
        if (Gender == 'Male'):
            Gender = 1

        else:
            Gender=0
        
        # Dependent_count
        Dependent_count = eval(request.form['Dependent_count'])

        # Education_Level
        Education_Level = request.form["Education_Level"]

        if (Education_Level == 'Uneducated'):
            Education_Level = 0

        elif (Education_Level == 'High_School'):
            Education_Level = 1
        
        elif (Education_Level == 'College'):
            Education_Level = 2
        elif (Education_Level == 'Graduate'):
            Education_Level = 3
        elif (Education_Level == 'Post-Graduate'):
            Education_Level = 4
        elif (Education_Level == 'Doctorate'):
            Education_Level = 5
        elif (Education_Level == 'Unknown'):
            Education_Level = 6

        # Marital_Status
        Marital_Status = request.form["Marital_Status"]
        
        if (Marital_Status == 'Single'):
            Marital_Status = 0

        elif (Marital_Status == 'Married'):
            Marital_Status = 1
        
        elif (Marital_Status == 'Divorced'):
            Marital_Status = 2
        elif (Marital_Status == 'Unknown'):
            Marital_Status = 3

         # Income_Category
        Income_Category = request.form["Income_Category"]
        
        if (Income_Category == 'Less_than_$40K'):
            Income_Category = 0

        elif (Income_Category == '$40K_$60K'):
            Income_Category = 1
        
        elif (Income_Category == '$60K_$80K'):
            Income_Category = 2
        elif (Income_Category == '$80K_$120K'):
            Income_Category = 3
        
        elif (Income_Category == '$120K+'):
            Income_Category = 4
        elif (Income_Category == 'Unknown'):
            Income_Category = 5  
        
        # Card_Category
        Card_Category = request.form["Card_Category"]
        
        if (Card_Category == 'Blue'):
            Card_Category = 0

        elif (Card_Category == 'Silver'):
            Card_Category = 1
        
        elif (Card_Category == 'Gold'):
            Card_Category = 2
        elif (Card_Category == 'Platinum'):
            Card_Category = 3

        # Months_on_book
        Months_on_book = eval(request.form['Months_on_book'])

        # Total_Relationship_Count
        Total_Relationship_Count = eval(request.form['Total_Relationship_Count'])

        # Months_Inactive_12_mon
        Months_Inactive_12_mon = eval(request.form['Months_Inactive_12_mon'])

        # Contacts_Count_12_mon
        Contacts_Count_12_mon = eval(request.form['Contacts_Count_12_mon'])

        # Credit_Limit
        Credit_Limit = eval(request.form['Credit_Limit'])

        # Total_Revolving_Bal
        Total_Revolving_Bal = eval(request.form['Total_Revolving_Bal'])

        # Avg_Open_To_Buy
        Avg_Open_To_Buy = eval(request.form['Avg_Open_To_Buy'])

        # Total_Amt_Chng_Q4_Q1
        Total_Amt_Chng_Q4_Q1 = eval(request.form['Total_Amt_Chng_Q4_Q1'])

        # Total_Trans_Amt
        Total_Trans_Amt = eval(request.form['Total_Trans_Amt'])

        # Total_Trans_Ct
        Total_Trans_Ct = eval(request.form['Total_Trans_Ct'])

        # Total_Ct_Chng_Q4_Q1
        Total_Ct_Chng_Q4_Q1 = eval(request.form['Total_Ct_Chng_Q4_Q1'])

        # Avg_Utilization_Ratio
        Avg_Utilization_Ratio = eval(request.form['Avg_Utilization_Ratio'])

        # prediction
    # try:
    #     result = model.predict([[45,0,3,1,1,2,0,39,5,1,3,12691,777,11914,1.335,1144,42,1.625,0.061]])
    # except Exception as e:
    #     print(e)

    result = model.predict([[Customer_Age, Gender,Dependent_count, Education_Level, Marital_Status,Income_Category, Card_Category,Months_on_book,Total_Relationship_Count,Months_Inactive_12_mon,Contacts_Count_12_mon, Credit_Limit, Total_Revolving_Bal, Avg_Open_To_Buy,Total_Amt_Chng_Q4_Q1, Total_Trans_Amt, Total_Trans_Ct, Total_Ct_Chng_Q4_Q1, Avg_Utilization_Ratio]])
    
    if result[0] == 1:
        result = 'Attrited : Customer is going to churn'
    else:
        result = 'Existing Customer: Customer not going to Churn'

    return result

    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)

    
# return render_template('index.html',result=result)




