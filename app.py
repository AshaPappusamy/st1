import sqlalchemy as sqlalchemy
engine = sqlalchemy.create_engine("mysql+mysqlconnector://3qKZvyc8Bw7Ckf1.root:ixPIapSBo4owm2Qf@gateway01.ap-southeast-1.prod.aws.tidbcloud.com:4000/Asteroids")
import sqlalchemy
import streamlit as st
st.write("This is my Heading")
st.write("hello")
st.set_page_config(page_title="NASA Asteroid Dashboard", layout="wide")
st.title("🚀 NASA Near-Earth Object (NEO) Insights")
import pandas as pd
from sqlalchemy import create_engine, text
