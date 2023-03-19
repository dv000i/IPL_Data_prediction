from flask import Flask, request
from flasgger import Swagger
import pickle


app = Flask(__name__)
Swagger(app)

@app.route("/")
def welcomwe():
    return "welcome"


pickle_in = open('ipl_data2.pickle', 'rb')
classifier = pickle.load(pickle_in)

@app.route('/predict', methods = ['POST'])
def predict():
    """ IPL Match Winner prediction
       This is using docstrings for specifications.
       ---
       parameters:
         -name:Batting Team
          in:query
          type:string
          enum:['Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab',
                'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
                'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
          description:"Enter Batting team."
          required:true
         -name:Bowling Team
          in:query
          type:string
          enum:['Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab',
                'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
                'Royal Challengers Bangalore', 'Sunrisers Hyderabad']
          description:"Enter Bowling team."
          required:true
         -name:Venue
          in:query
          type:string
          enum:['Barabati Stadium', 'Brabourne Stadium', 'Buffalo Park',
                   'De Beers Diamond Oval', 'Dr DY Patil Sports Academy',
                   'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
                   'Dubai International Cricket Stadium', 'Eden Gardens',
                   'Feroz Shah Kotla', 'Himachal Pradesh Cricket Association Stadium',
                   'Holkar Cricket Stadium', 'JSCA International Stadium Complex',
                   'Kingsmead', 'M Chinnaswamy Stadium', 'M.Chinnaswamy Stadium',
                   'MA Chidambaram Stadium, Chepauk',
                   'Maharashtra Cricket Association Stadium', 'New Wanderers Stadium',
                   'Newlands', 'OUTsurance Oval',
                   'Punjab Cricket Association IS Bindra Stadium, Mohali',
                   'Punjab Cricket Association Stadium, Mohali',
                   'Rajiv Gandhi International Stadium, Uppal',
                   'Sardar Patel Stadium, Motera', 'Sawai Mansingh Stadium',
                   'Shaheed Veer Narayan Singh International Stadium',
                   'Sharjah Cricket Stadium', 'Sheikh Zayed Stadium',
                   "St George's Park", 'Subrata Roy Sahara Stadium',
                   'SuperSport Park', 'Vidarbha Cricket Association Stadium, Jamtha',
                   'Wankhede Stadium']
          description:"Enter Match Venue."
          required:true
         - name:Target
            in:query
            type:number
            required:true
         - name:Current Runs
            in:query
            type:number
            required:true
         - name:Balls Left
            in:query
            type:number
            required:true
         - name:Runs Left
            in:query
            type:number
            required:true
         - name:Wicket Left
            in:query
            type:number
            required:true
         - name:Current Run Rate
            in:query
            type:Double
            required:true
         - name:Required Run Rate
            in:query
            type:double
            required:true
       responses:
           200:
               description: The Predicted Wining team

       """

    bat = request.args.get('Batting Team')
    bol = request.args.get('Bowling Team')
    ven = request.args.get('Venue')
    tar = request.args.get('Target')
    cur = request.args.get('Current Runs')
    balf = request.args.get('Balls Left')
    wic = request.args.get('Wickets Left')
    curr = request.args.get('Current Run Rate')
    reqr = request.args.get('Required Run Rate')

    prediction = classifier.predict([[bat, bol, ven, tar, cur, balf, wic, curr, reqr]])

    return prediction


if __name__ == '__main__':
    app.run()