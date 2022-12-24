import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from air_quality_plot import plot_air_quality
from pollution_etl import get_pollution_data, rename_columns, cleaning_columns, get_current_pollution
st.set_option('deprecation.showPyplotGlobalUse', False)

now = int((datetime.now() - timedelta(minutes=1)).timestamp())
week_earlier = int((datetime.now() - timedelta(days=7)).timestamp())

# Load the data
data = get_pollution_data(week_earlier, now, 49.9778328, 18.9425124)
data = cleaning_columns(data)
data = rename_columns(data)

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
