from flask import Flask, request
import streamlit as st

import pickle
import pandas as pd
import numpy as np

import numpy as np
import pandas as pd

app = Flask(__name__)

pickle_in = open('ipl_data2.pickle', 'rb')
classifier = pickle.load(pickle_in)


def predict(bat, bol, ven, tar,run, cur, balf, wic, curr, reqr):
    prediction = classifier.predict([[bat, bol, ven, tar, run, cur, balf, wic, curr, reqr]])

    return prediction


array = np.array(['Barabati Stadium', 'Brabourne Stadium', 'Buffalo Park',
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
                  'Wankhede Stadium'])
df = pd.DataFrame(data=array)

array2 = np.array(['Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab',
                   'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals',
                   'Royal Challengers Bangalore', 'Sunrisers Hyderabad'])
df2 = pd.DataFrame(data=array2)


def main():
    st.title("IPL Prediction")

    st.markdown("Venue code")
    st.dataframe(df, height=500,width=500)
    st.markdown("Team code")
    st.dataframe(df2, height=300,width=500)

    bat = st.text_input("Batting team code")
    bol = st.text_input("Bowling team code")
    ven = st.text_input("Venue code")
    tar = st.text_input("Target")
    run = st.text_input("Current runs")
    cur = st.text_input("Runs Left")
    balf = st.text_input("Balls left")
    wic = st.text_input("Wickets left")
    curr= st.text_input("Current run rate")
    reqr = st.text_input("Required run rate")

    result = ""
    if st.button("Predict"):
        result = predict(bat,bol,ven,tar,run,cur,balf,wic,curr,reqr)

    st.success("output is {} ".format(result))


if __name__ == '__main__':
    main()
