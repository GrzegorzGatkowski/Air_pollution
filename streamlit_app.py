import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
from air_quality_plot import plot_air_quality
from pollution import get_pollution_data
st.set_option('deprecation.showPyplotGlobalUse', False)

today = datetime.date.today()
print(today)

# Load the data
data = get_pollution_data("2022-12-15", "2022-12-16", 49.9778328, 18.9425124)

# Create a list of columns to choose from
column_options = ['Carbon Monoxide_(CO)', 'Nitric oxide_(NO)',
       'Nitrogen Dioxide_(NO2)', 'Ozone_(O3)', 'Sulfur Dioxide_(SO2)', 'PM2_5',
       'PM10', 'NH3']

# Create a multiple select widget for the user to choose which columns to plot
selected_columns = st.multiselect("Select columns to plot", column_options)

# Plot the selected columns
if selected_columns:
       fig, ax = plt.subplots()
       fig = plot_air_quality(data, selected_columns, 'Air Quality', 'Date', 'Pollutant concentration in μg/m3', 'red', 'dark')
       st.write("Here is a Seaborn plot:")
       st.pyplot(fig)
