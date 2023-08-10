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

st.subheader("Introduction : ")

#Lucy
#Does smoking increase the number of awakenings during the night? Histogram of Awakenings with Smoking as Hue
st.subheader("Does smoking decrease Sleep Efficiency during the night?")
cross_tab_prop = pd.crosstab(index=df['Sleep efficiency'],
                             columns=df['Smoking status'],
                             normalize="index")
# Create a Streamlit app
st.title("Sleep Efficiency vs. Smoking Status")
st.write("Cross Tabulation:")
#st.write(cross_tab_prop.head())
# Create the bar plot
st.write("Bar Plot:")
fig, ax = plt.subplots(figsize=(10, 6))
cross_tab_prop.plot(kind='bar', stacked=True, colormap='tab10', ax=ax)
plt.legend(loc="upper left", ncol=2)
plt.xlabel("Sleep efficiency")
plt.ylabel("Proportion")
st.pyplot(fig)
st.text(
  "We wanted to see whether smoking would have an effect on people's sleep quality. Our data showed that the proportion of people who smoked was higher in people who had worse sleep quality, likely since the substances found in cigarettes like nicotine can disrupt sleep and act as a stimulant."
)

#Does age impact one's quality of sleep? Scatterplot
# Define age groups and labels
Age_Group = [(9, 21, 'Young'), (22, 34, 'Younger Adult'),
             (35, 47, 'Middle Aged'), (48, 69, 'Older')]


def assign_age_group(age):
  for start, end, label in Age_Group:
    if start <= age <= end:
      return label
  return 'Unknown'


df['Age-Group'] = df['Age'].apply(assign_age_group)
#Write title
st.subheader("Does one's age have an impact on their sleep efficiency?")
#Create Graph
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Age-Group", y="Sleep efficiency", marker="o", ax=ax)
plt.xlabel("Age Group")
plt.ylabel("Sleep Efficiency")
st.pyplot(fig)
#Write Summary
st.write(
  "Although we expected one's quality of sleep to deteriorate as they aged, as people's health generally decreases as they get older, our data showed the opposite. As one's age increased, their sleep efficiency did the same, and younger people tended to suffer from lower sleep efficiency. While this could be due to increasing stress amoung teens which leads to lower sleep rates, it could also be a result of the influence of other factors."
)
#Do people who go to bed later or earlier have a better quality of sleep? Scatterplot

df['Bedtime'] = pd.to_datetime(df['Bedtime'])
df['Wakeup time'] = pd.to_datetime(df['Wakeup time'])
# Convert bedtime and wakeup time to hours, considering AM/PM
df['Bedtime'] = (df['Bedtime'].dt.hour % 12) + (df['Bedtime'].dt.minute / 60)
df['Bedtime'] = df['Bedtime'].apply(lambda x: x if x < 12 else x - 12)
df['Bedtime'] = df['Bedtime'].apply(lambda x: x * -1 if x > 6 else x)

df['Wakeup time'] = (df['Wakeup time'].dt.hour %
                     12) + (df['Wakeup time'].dt.minute / 60)
df['Wakeup time'] = df['Wakeup time'].apply(lambda x: x if x < 12 else x - 12)
sns.lineplot(data=df, x="Bedtime", y="Sleep efficiency")
In general, those who went to bed earlier had a greater sleep efficiency, although the negative trend was less pronounced than we thought, and was pretty variable.
#Do people who exercise regularly get more sleep? Scatterplot, LinePlot

#Blythe

#How caffeine consumption relates to sleep efficiency? Scatterplot
st.subheader("How caffeine consumption relates to sleep efficiency? ")

fig = px.scatter(df,
                 x="Sleep efficiency",
                 y="Caffeine consumption",
                 color="Gender")

st.plotly_chart(fig)
st.write(
  "In general, those who went to bed earlier had a greater sleep efficiency, although the negative trend was less pronounced than we thought, and was pretty variable."
)
st.text(
  "There doesn't seem to be much correlation between a person's caffeine consumption and their sleep efficiency as we originally thought. It is pretty varied the amount of sleep efficiency people have, no matter their caffeine consumption."
)

#Do people who get less REM sleep tend to drink more caffeine? Scatterplot
st.subheader("Do people who get less REM sleep tend to drink more caffeine?")

fig = px.scatter(df,
                 x="Caffeine consumption",
                 y="REM sleep percentage",
                 color="Gender")

st.plotly_chart(fig)

st.text(
  "The data shows that people's caffeine consumption isn't necessarily effected by their REM sleep percentage and vice versa. There seems to be a steady number of people getting the same amount of REM sleep no matter their caffeine consumption."
)

#Is age related to bedtime/wakeup time? ScatterPlot, Histogram
st.subheader("Is age related to bedtime/wakeup time?")

df['Bedtime'] = pd.to_datetime(df['Bedtime'])
df['Wakeup time'] = pd.to_datetime(df['Wakeup time'])

# Convert bedtime and wakeup time to hours, considering AM/PM
df['Bedtime'] = (df['Bedtime'].dt.hour % 12) + (df['Bedtime'].dt.minute / 60)
df['Bedtime'] = df['Bedtime'].apply(lambda x: x if x < 12 else x - 12)
df['Bedtime'] = df['Bedtime'].apply(lambda x: x * -1 if x > 6 else x)

df['Wakeup time'] = (df['Wakeup time'].dt.hour %
                     12) + (df['Wakeup time'].dt.minute / 60)
df['Wakeup time'] = df['Wakeup time'].apply(lambda x: x if x < 12 else x - 12)

fig, ax = plt.subplots()
sns.histplot(data=df, x='Bedtime', hue="Age-Group", multiple="stack", ax=ax)
plt.xlabel("Bedtime")
plt.ylabel("Count")
st.pyplot(fig)

st.text(
  "Based on the histogram, people of older age seem to go to bed at a later time. There are two fairly distinct time slots where the younger group tend to go to bed before midnight, and the older group stay up past."
)

fig, ax = plt.subplots()
sns.histplot(data=df,
             x='Wakeup time',
             hue="Age-Group",
             multiple="stack",
             ax=ax)
plt.xlabel("Wake-Up Time")
plt.ylabel("Count")
st.pyplot(fig)

st.text(
  "The wakeup times are more varried, not necessarily being devided by age. There are people from each group waking up at different hours of the morning, but the 'Old' do appear to sleep in later than the younger groups."
)
#Does gender play a role in how long or the quality of one's sleep? Histogram
st.subheader(
  "Does gender play a role in how long or the quality of one's sleep?")

sns.histplot(df, x = 'Sleep efficiency', hue = 'Gender')

st.subheader("Conclusion : ")
