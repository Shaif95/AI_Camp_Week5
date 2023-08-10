import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings
#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("Radiant_Raspberries")

df = pd.read_csv("Sleep_Efficiency.csv")

st.write(df.head(2))

#Lucy 
#Does smoking increase the number of awakenings during the night? Histogram of Awakenings with Smoking as Hue

st.write("Does smoking increase the number of awakenings during the night?")


#Does age impact one's quality of sleep? Scatterplot


#Do people who go to bed later or earlier have a better quality of sleep? Scatterplot



#Do people who exercise regularly get more sleep? Scatterplot, LinePlot



#Blythe

#How caffeine consumption relates to sleep efficiency? Scatterplot
st.write("How caffeine consumption relates to sleep efficiency? ")

#Do people who get less REM sleep tend to drink more caffeine? Scatterplot
st.write("Do people who get less REM sleep tend to drink more caffeine?")

#Is age related to bedtime/wakeup time? ScatterPlot, Histogram
st.write("Is age related to bedtime/wakeup time?")

#Does gender play a role in how long or the quality of one's sleep? Histogram
st.write("Does gender play a role in how long or the quality of one's sleep?")