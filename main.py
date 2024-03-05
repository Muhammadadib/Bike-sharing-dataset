import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Load Day Data csv
url = "https://raw.githubusercontent.com/Muhammadadib/Bike-sharing-dataset/main/Dataset/day.csv"
day_df = pd.read_csv(url)

datetime_columns = ["order_date", "delivery_date"]
st.title("Proyek Analisis Data")

# Title for the app
st.subheader("Table Bike Sharing Data")

# Display DataFrame as a table (optional)
st.dataframe(day_df)

st.subheader("Bike Sharing Data - dteday vs cnt")
# Extract the desired columns
dteday = day_df["dteday"]
cnt = day_df["cnt"]

# Create the plot
fig, ax = plt.subplots()  # Create figure and axis objects
ax.plot(dteday, cnt)  # Plot dteday vs cnt

# Label the axes
ax.set_xlabel("dteday")
ax.set_ylabel("cnt")

# Add a title to the plot
ax.set_title("dteday vs cnt")

# Display the plot using Streamlit
st.pyplot(fig)

st.title("Bike Sharing Data - season vs cnt")
# Assuming the "season" column exists with the specified mapping
season_mapping = {1: "Spring", 2: "Summer", 3: "Autumn", 4: "Winter"}

# Replace the original "season" values with the corresponding season names
day_df['season'] = day_df['season'].replace(season_mapping)

# Display plot distribution of season vs cnt graphic
fig, ax = plt.subplots()
season_counts = day_df['season'].value_counts()
ax.pie(season_counts, labels=season_counts.index, autopct="%1.1f%%")
st.pyplot(fig)

# Display season counts
st.subheader("Season vs Count Distribution Table")
st.write(day_df['season'].value_counts())

weather_mapping = {
    1: "Clear",
    2: "Mist",
    3: "Snow",
    # Add other mappings as needed
}

st.title("Bike Sharing Data - weather vs count")
# Create a new column named "weather" to store the classified weather type
day_df["weathersit"] = day_df["weathersit"].replace(weather_mapping)

# Create the scatter plot
fig, ax = plt.subplots()
season_counts = day_df['weathersit'].value_counts()
ax.pie(season_counts, labels=season_counts.index, autopct="%1.1f%%")

# Label the axes
ax.set_xlabel("weathersit")
ax.set_ylabel("cnt")

# Add a title to the plot
ax.set_title("weathersit vs cnt")

# Display the plot using Streamlit
st.pyplot(fig)

# Display weather counts
st.subheader("Weather vs Count Distribution Table")
st.write(day_df['weathersit'].value_counts())

# Assuming the "weekday" and "cnt" columns exist
weekday_column = "weekday"
cnt_column = "cnt"

# Define the reversed working day mapping
weekday_mapping = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
}

# Apply the mapping to create a new "weekday_label" column
day_df["weekday_label"] = day_df[weekday_column].replace(weekday_mapping)

# Calculate average cnt by working day label
average_cnt_by_weekday = day_df.groupby("weekday_label")[cnt_column].mean()

# Title for the app
st.title("Bike Sharing Data - weekday vs cnt")

# Create the bar chart
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(average_cnt_by_weekday.index, average_cnt_by_weekday.values)

# Label the axes
ax.set_xlabel("Working Day")
ax.set_ylabel("Average cnt")

# Add a title to the plot
ax.set_title("weekday vs cnt")

# Customize the plot (optional)
ax.grid(axis="y")  # Add grid lines on the y-axis

# Rotate x-axis labels for better readability
ax.set_xticks(average_cnt_by_weekday.index, labels=average_cnt_by_weekday.index, rotation=45)  # Explicitly pass labels

# Display the plot using Streamlit
st.pyplot(fig)

# Display weather counts
st.subheader("Weekday vs Count Distribution Table")
st.write(day_df['weekday'].value_counts())

# Assuming the "weekday" and "cnt" columns exist
workingday_column = "workingday"
cnt_column = "cnt"

# Define the reversed working day mapping
workingday_mapping = {
    0: "Holiday",
    1: "Weekday",
}

# Apply the mapping to create a new "workingday" column
day_df["workingday"] = day_df[workingday_column].replace(workingday_mapping)

# Calculate average cnt by working day label
average_cnt_by_workingday = day_df.groupby("workingday")[cnt_column].mean()

# Title for the app
st.title("Bike Sharing Data - workingday vs cnt")

# Create the bar chart
fig, ax = plt.subplots(figsize=(8, 6))
ax.bar(average_cnt_by_workingday.index, average_cnt_by_workingday.values)

# Label the axes
ax.set_xlabel("WorkingDay")
ax.set_ylabel("Cnt")

# Add a title to the plot
ax.set_title("workingday vs cnt")

# Customize the plot (optional)
ax.grid(axis="y")  # Add grid lines on the y-axis

# Rotate x-axis labels for better readability
ax.set_xticks(average_cnt_by_workingday.index, labels=average_cnt_by_workingday.index, rotation=45)  # Explicitly pass labels

# Display the plot using Streamlit
st.pyplot(fig)

# Display weather counts
st.subheader("Workingday vs Count Distribution Table")
st.write(day_df['workingday'].value_counts())

st.caption('Copyright © Madifa 2024')