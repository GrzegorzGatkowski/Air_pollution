from pollution import get_current_pollution, cleaning_columns, rename_columns

points = [[18.69226443293215,50.04458130627151],[18.714421831068705,49.960425484595135],[18.759743781803053,49.915698304318255],[19.0064966246905,49.90532085372911],[19.15152686704164,49.98050678867074],[19.21397044360944,50.03552544963239],[18.9329743490552,50.06074823030394],[18.783915488862107,50.036172353185066],[18.69226443293215,50.04458130627151]]
df = get_current_pollution(points)
df = cleaning_columns(df)
df = rename_columns(df)

print(df.head(10))

print(df.columns)

import plotly.express as px

# create a figure object with the surfacemapbox trace type
fig = px.scatter_mapbox(df, lon="coord.lat", lat="coord.lon", color="PM2_5", title="Air Pollution",
                        color_continuous_scale='magma', zoom=10, mapbox_style="open-street-map",
                        height=500, width=800,
                        hover_name="PM2_5", hover_data=["coord.lat", "coord.lon", "PM2_5"], 
                        )

# Show the figure
fig.show()
