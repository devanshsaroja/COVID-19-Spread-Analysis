import folium
import pandas as pd
import branca
from flask import Flask, render_template

app = Flask(__name__)

# Define the dataset path here so you can change it easily
DATASET_PATH = 'covid-19-dataset-1.csv'  # Change this filename as needed

# Function to create a folium map with circles
def create_folium_map():
    corona_df = pd.read_csv(DATASET_PATH)
    corona_df = corona_df[['Lat', 'Long_', 'Confirmed', 'Country_Region']].dropna()

    # Create the map
    m = folium.Map(location=[34.223334, -82.461707], tiles='CartoDB positron', zoom_start=8)

    # Function to create circles on the map
    def circle_maker(x):
        confirmed_cases = float(x.iloc[2])
        radius = confirmed_cases * 0.5  # Scaling factor for circle size
        if radius < 5:
            radius = 5  # Minimum radius to avoid disappearing circles

        folium.Circle(
            location=[x.iloc[0], x.iloc[1]],
            radius=radius,
            color='red',
            fill=True,
            fill_color='red',  # Fill color for the circle
            fill_opacity=0.6,  # Transparency
            popup='{}: Confirmed cases: {}'.format(x.iloc[3], confirmed_cases)
        ).add_to(m)

    corona_df.apply(lambda x: circle_maker(x), axis=1)

    # Return the map HTML representation for embedding
    return m._repr_html_()

# Function to fetch the top 15 countries based on confirmed cases
def find_top_confirmed(n=15):
    corona_df = pd.read_csv(DATASET_PATH)
    by_country = corona_df.groupby('Country_Region').sum()[['Confirmed', 'Deaths', 'Recovered', 'Active']]
    cdf = by_country.nlargest(n, 'Confirmed')[['Confirmed']]
    return cdf

# Main route for Flask
@app.route('/')
def home():
    cdf = find_top_confirmed()
    pairs = [(country, confirmed) for country, confirmed in zip(cdf.index, cdf['Confirmed'])]
    
    # Create the map
    html_map = create_folium_map()

    # Render home.html with the necessary data
    return render_template("home.html", table=cdf, cmap=html_map, pairs=pairs)

if __name__ == "__main__":
    app.run(debug=True)
