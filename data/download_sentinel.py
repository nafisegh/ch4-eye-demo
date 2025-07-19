
import geopandas as gpd
import requests
import os


# --- 1. Load AOI from your local geojson file ---
aoi = gpd.read_file("data/aoi.geojson").to_crs(4326)
aoi_bounds = aoi.total_bounds # [minx, mine, maxxx, maxy]

# --- 2. List of known Sentinel-2 title IDs that cover Turkmenistan (example: 42S, 43S,43T, etc.)---
# For demo, we use title 42SYF (you can extend this)

title = {
	"utm": "42",
        "lat_band": "S",
        "grid_square": "YF"
}

# --- 3. Set the desired date (in format YYY/MM/DD) ---
year = "2024"
month = "6"
day  = "26" # You can loop through days if needed

# --- 4. Construct AWS S3 Path ---
s3_path = f"s3://sentinel-s2-l1c/tiles/{title['utm']}/{title['lat_band']}/{title['grid_square']}/{year}/{month}/{day}/0/"  

# --- 5. Define local folder to download into ---
local_folder = "data/sentinel_scenes"
os.makedirs(local_folder, exist_ok=True) 

# --- 6. Create and write s5cmd command script ---
download_script_path = os.path.join("data", "download_s2_from_aws.sh")
with open("data/download_s2_from_aws.sh", "w") as f:
    f.write("#!/bin/bash\n")
    f.write("s5cmd --no-sign-request cp "
            "\"s3://sentinel-s2-l1c/tiles/42/S/YF/2024/6/26/0/B08.jp2\" "
            "\"data/sentinel_scenes/20240626_B08.jp2\"\n")
    f.write("s5cmd --no-sign-request cp "
            "\"s3://sentinel-s2-l1c/tiles/42/S/YF/2024/6/26/0/metadata.xml\" "
            "\"data/sentinel_scenes/20240626_metadata.xml\"\n")

print("Download script saved to:", download_script_path)
print("To download, run:")
print(f"sh {download_script_path}")
