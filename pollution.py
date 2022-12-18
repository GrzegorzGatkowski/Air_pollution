import requests
import pandas as pd
import streamlit as st
import datetime


def get_pollution_data(start_time, end_time, lat, lon):
    """
    Retrieve air pollution data from the OpenWeatherMap API for a specified time range and location.
    Parameters:
        start_time (str): The start time for the data range, in the format "YYYY-MM-DD".
        end_time (str): The end time for the data range, in the format "YYYY-MM-DD".
        lat (float): The latitude of the location for which to retrieve data.
        lon (float): The longitude of the location for which to retrieve data.
    Returns:
        pandas.DataFrame: A dataframe containing the API response data.
    """

    start = int(datetime.datetime.strptime(start_time, "%Y-%m-%d").timestamp())
    end = int(datetime.datetime.strptime(end_time, "%Y-%m-%d").timestamp())

    # API endpoint and API key
    api_endpoint = "https://api.openweathermap.org/data/2.5/air_pollution/history"
    api_key = st.secrets["api_key"]

    # Send the API request
    response = requests.get(api_endpoint, params={
        "lat": lat,
        "lon": lon,
        "start": start,
        "end": end,
        "appid": api_key
    })

    # Check for errors
    if response.status_code != 200:
        print("Error: API request failed with status code", response.status_code)
        exit()

    # Parse the API response
    data = response.json()

    # Convert the data to a dataframe
    df = pd.json_normalize(data['list'])

    # Dropping and renaming columns
    df.drop(columns='main.aqi', inplace=True)
    df['dt'] = pd.to_datetime(df['dt'], unit='s')
    df.set_index('dt', inplace = True)
    df = df.rename(columns={'components.co': 'Carbon Monoxide_(CO)', 'components.no': 'Nitric oxide_(NO)', 'components.no2': 'Nitrogen Dioxide_(NO2)',
                        'components.o3': 'Ozone_(O3)', 'components.so2': 'Sulfur Dioxide_(SO2)', 'components.pm2_5': 'PM2_5',
                        'components.pm10': 'PM10', 'components.nh3': 'NH3'})

    return df
