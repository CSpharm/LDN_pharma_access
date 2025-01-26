from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import pandas as pd
import time

# Load the cleaned dataset
file_path = '../data/london_pharmacies_cleaned.csv'
df = pd.read_csv(file_path)

# Initialize Geopy's Nominatim service
geolocator = Nominatim(user_agent="pharmacy_mapper")

# Function to fetch latitude and longitude
def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None, None
    except GeocoderTimedOut:
        time.sleep(1)
        return geocode_address(address)

# Apply the geocode function to the Address column
df[['Latitude', 'Longitude']] = df['Address'].apply(lambda x: pd.Series(geocode_address(x)))

# Save the dataset with coordinates
geocoded_file_path = '../data/london_pharmacies_geocoded.csv'
df.to_csv(geocoded_file_path, index=False)

print(f"Geocoded data saved to '{geocoded_file_path}'.")