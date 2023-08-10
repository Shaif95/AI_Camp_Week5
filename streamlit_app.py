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

st.header("Does smoking increase the number of awakenings during the night?")
cross_tab = pd.crosstab(index=df['Sleep efficiency'],
                        columns=df['Smoking status'])
cross_tab.head(1)
cross_tab_prop.plot(kind='bar', 
                    stacked=True, 
                    colormap='tab10', 
                    figsize=(10, 6))

plt.legend(loc="upper left", ncol=2)
plt.xlabel("Sleep efficiency")
plt.ylabel("Proportion")
plt.show()
st.text("We also wanted to see whether smoking would have an effect on people's sleep quality. Our data showed that the proportion of people who smoked was higher in people who had worse sleep quality, likely since the substances found in cigarettes like nicotine can disrupt sleep and act as a stimulant.")
#Does age impact one's quality of sleep? Scatterplot


#Do people who go to bed later or earlier have a better quality of sleep? Scatterplot



#Do people who exercise regularly get more sleep? Scatterplot, LinePlot



#Blythe

#How caffeine consumption relates to sleep efficiency? Scatterplot
st.header("How caffeine consumption relates to sleep efficiency? ")

#Do people who get less REM sleep tend to drink more caffeine? Scatterplot
st.header("Do people who get less REM sleep tend to drink more caffeine?")

#Is age related to bedtime/wakeup time? ScatterPlot, Histogram
st.header("Is age related to bedtime/wakeup time?")

#Does gender play a role in how long or the quality of one's sleep? Histogram
st.header("Does gender play a role in how long or the quality of one's sleep?")