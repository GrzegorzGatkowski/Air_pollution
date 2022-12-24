Built by [grzegorzgatkowski](https://github.com/grzegorzgatkowski)

# Air Pollution Data Engineering Project
This project retrieves air pollution data from the OpenWeatherMap API for the city of Pszczyna, Poland and stores it in S3 buckets using Apache Airflow. The data is then visualized and analyzed using Seaborn and Streamlit.

## Data
The data for this project consists of air pollution measurements for the city of Pszczyna, Poland. The data includes the following fields:

Carbon Monoxide (CO)
Nitric oxide (NO)
Nitrogen Dioxide (NO2)
Ozone (O3)
Sulfur Dioxide (SO2)
PM2.5 (particulate matter with a diameter of 2.5 micrometers or less)
PM10 (particulate matter with a diameter of 10 micrometers or less)
NH3 (ammonia)
coord.lon (longitude)
coord.lat (latitude)
These pollutants are measured in order to calculate the air quality index (AQI) for the city. The AQI is a measure of the concentration of air pollutants in the air, and is calculated based on the levels of the above pollutants. The AQI can range from 0 (good air quality) to over 500 (hazardous air quality). You can find more information about the AQI and the different pollutants that contribute to it on Wikipedia.

## Analysis
The data is analyzed to understand trends and patterns in air pollution levels over time in Pszczyna. The visualizations created using Seaborn and Streamlit allow users to explore the data and gain insights into the state of air pollution in the city.

## Requirements
To run this project, you will need the following software:

Python 3.x
Apache Airflow
Seaborn
Streamlit
You will also need an API key from OpenWeatherMap.

## Setup

```sh
# External users: download Files
git clone git@github.com:grzegorzgatkowski/Air_pollution.git

# Go to correct directory
cd Air_pollution
# Run the streamlit app (will install dependencies in a virtualenvironment in the folder venv)
make run
```

Install the required Python packages using pip install -r requirements.txt.

Set up Apache Airflow and configure the DAG to retrieve data from the OpenWeatherMap API and store it in S3.

Run the Streamlit app to visualize and analyze the data.
Open your browser to [http://localhost:8501/](http://localhost:8501/) if it doesn't open automatically.

## Contribution
We welcome contributions to this project! If you have an idea for improving the data engineering pipeline or the data analysis, please feel free to open a pull request.

## Acknowledgements
This project would not have been possible without the data provided by the OpenWeatherMap API. We would like to thank them for making this data available to the public.

