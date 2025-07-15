<<<<<<< HEAD

=======
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date
import os


# Define credentials for Copernicus Open Access Hub (register for free)
USERNAME = nafise.ghasemian@gmail.com
PASSWORD = @Gnafisegh123

# Connect to API
api = SentinelAPI(USERNAME, PASSWORD, 'https://scihub.copernicus.eu/dhus')

# Load area of interest (AOI)
Footprint = geojson_to_wkt(read_geojson('data/aoi.geojson'))

# Search for products

Products = api.query(footprint, data=('20240601', '20240630'),
		    platform='Sentinel-2',
                    cloudcoveragepercentage=(0,10),
                    processinglevel='Level-1C')

# Print results
print(f"Found {len(products)} products.")
for uuid, prod in products.items():
    print(f"{prod['title']} - {prod['beginposition']}")

# Optionally: download metadata or manually selected tile
for uuid in list(products.keys())[:1]: # change [:1] to [:3] to download 3 scenes
    api.download(uuid, directory_path='data/raw')	
	
>>>>>>> cb42945 (Added Sentinel-2 download script to downaload-sentinel.py)
