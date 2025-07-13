import sqlalchemy as sqlalchemy_package
from sqlalchemy import create_engine, text
engine = sqlalchemy_package.create_engine("mysql+mysqlconnector://3qKZvyc8Bw7Ckf1.root:ixPIapSBo4owm2Qf@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/Asteroids")
import streamlit as st
import pandas as pd
st.write("This is my Heading")
st.write("hello")
st.set_page_config(page_title="NASA Asteroid Dashboard", layout="wide")
st.title("🚀 NASA Near-Earth Object (NEO) Insights")
# Dropdown for selecting query
query_options = [
    "1. Count how many times each asteroid has approached Earth",
    "2. Average velocity of each asteroid",
    "3. Top 10 fastest asteroids",
    "4. Hazardous asteroids that approached > 3 times",
    "5. Month with most asteroid approaches",
    "6. Fastest ever approach",
    "7. Sort asteroids by max diameter",
    "8. Asteroids getting closer over time",
    "9. Closest approach per asteroid",
    "10. Velocity > 50,000 km/h",
    "11. Approach count per month",
    "12. Brightest asteroid",
    "13. Hazardous vs Non-Hazardous count",
    "14. Passed closer than 1 lunar distance",
    "15. Passed within 0.05 AU"
]

selected_query = st.selectbox("Select a query to run:", query_options)




