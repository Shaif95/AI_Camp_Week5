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

st.write(
  "Hi! My name is Blythe, I'm a grade 11 student from Ontario, Canada. I became interested in AI camp when I heard through my school that they were giving scholarships for their summer programs. I signed up because I want to study coding, and hope this camp will give me a head-start in my learning."
)

st.write(
  "Hi! My name is Lucy, and i'm a rising sophmore. I heard about AI camp from a teacher, and decided to take AI camp since I want to learn more about coding in python as well as how AI is being built and used."
)

st.subheader("Introduction : ")

st.write(
  "This data set is a collection of information aquired from 452 unique test subjects and information about their sleep patterns. It contains data about how well a person slept and how long, as well as information about their lives such as their age, gender, and if they smoke or drink. We used this dataset to analyze trends within the data, and used those trends to determine how different aspects of one's life impacts their sleep."
)

df = pd.read_csv("Sleep_Efficiency.csv")

st.write(df.head(2))

#Lucy
#Does smoking increase the number of awakenings during the night? Histogram of Awakenings with Smoking as Hue
st.subheader("Does smoking decrease Sleep Efficiency during the night?")
cross_tab_prop = pd.crosstab(index=df['Sleep efficiency'],
                             columns=df['Smoking status'],
                             normalize="index")
# Create a Streamlit app
st.write("Sleep Efficiency vs. Smoking Status")
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
st.write(
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
st.subheader(
  "Do people who go to bed later or earlier have a better quality of sleep?")
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
sns.lineplot(data=df, x="Bedtime", y="Sleep efficiency", ax=ax)

# Set x-axis label and y-axis label
plt.xlabel("Bedtime")
plt.ylabel("Sleep Efficiency")

# Adjust the x-axis tick label font size
ax.tick_params(axis='x', labelsize=5)

# Display the plot using Streamlit
st.pyplot(fig)

st.write(
  "In general, those who went to bed earlier had a greater sleep efficiency, although the negative trend was less pronounced than we thought, and was pretty variable."
)
#Do people who exercise regularly get more sleep? Scatterplot, LinePlot
st.subheader(
  "Do people who exercise regularly get more sleep?")

fig, ax = plt.subplots()
sns.lineplot(
    data=df,
    x = 'Exercise frequency', y = 'Sleep efficiency', ax=ax)
plt.xlabel("Excercise frequency")
plt.ylabel("Sleep Efficiency")
ax.tick_params(axis='x', labelsize=5)
st.pyplot(fig)
st.write("The correlation between better sleep and frequent excersize has been endorsed by many scientists and health reaserchers. Our data also demonstrates a connection between the efficiency of peoples' sleep and how often they excersized, with a positive curve showing that many of the people who excersized more often found themselves sleeping better.")
#Blythe

#How caffeine consumption relates to sleep efficiency? Scatterplot
st.subheader("How caffeine consumption relates to sleep efficiency? ")

fig = px.scatter(df,
                 x="Sleep efficiency",
                 y="Caffeine consumption",
                 color="Gender")

st.plotly_chart(fig)
st.write(
  "There doesn't seem to be much correlation between a person's caffeine consumption and their sleep efficiency as we originally thought. It is pretty varied the amount of sleep efficiency people have, no matter their caffeine consumption."
)

#Do people who get less REM sleep tend to drink more caffeine? Scatterplot
st.subheader("Do people who get less REM sleep tend to drink more caffeine?")

fig = px.scatter(df,
                 x="Caffeine consumption",
                 y="REM sleep percentage",
                 color="Gender")

st.plotly_chart(fig)

st.write(
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

g = sns.FacetGrid(data=df, col="Age-Group", margin_titles=True)
g.map_dataframe(sns.histplot, x='Bedtime', multiple="stack")
g.set_axis_labels("Bedtime", "Count")
g.set_titles(col_template="{col_name}")
st.pyplot(g)
st.write(
  "Based on the histogram, people of older age seem to go to bed at a later time. There are two fairly distinct time slots where the younger group tend to go to bed before midnight, and the older group stay up past. However, this is not necesarily caused by age, moreso the freedoms that come with getting older."
)

#Does gender play a role in how long or the quality of one's sleep? Histogram
st.subheader(
  "Does gender play a role in how long or the quality of one's sleep?")

fig, ax = plt.subplots()
sns.histplot(data=df,
             x='Sleep efficiency',
             hue="Gender",
             multiple="stack",
             ax=ax)
plt.xlabel("Sleep efficienct")
plt.ylabel("Count")
st.pyplot(fig)

st.write(
  "In the histogram, the columns are pretty evenly spread on how much sleep efficiency males and females get. Most males however, seem to get a larger amount sleep efficiency, in the 0.7 to 0.9 range. Whereas females are pretty evenly distributed through the scale with a spike at the 0.9 range"
)

fig, ax = plt.subplots()
sns.histplot(data=df,
             x='Sleep duration',
             hue="Gender",
             multiple="stack",
             ax=ax)
plt.xlabel("Sleep duration")
plt.ylabel("Count")
st.pyplot(fig)

st.write(
  "Similar to the histogram comparing gender and sleep efficiency, the columns are pretty even on comparing gender and sleep duration. There isn't any time that more males or females tend to sleep."
)

st.subheader("Conclusion : ")
st.write(
  "This dataset allowed us to make several connections and draw conclusions about the relationships between different aspects of people's lives and their sleep patterns. We found that smoking often leads to a less efficient sleep, while excersizing frequently and going to bed early makes one's sleep more efficient. We also found that sleep quality tends to improve with age, but that older people tended to go to bed at later times. Meanwhile, we found that there was little correlation between caffiene consumption and sleep quality."
)
