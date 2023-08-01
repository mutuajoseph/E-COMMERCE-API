import requests
# import settings
from settings.config import settings

API_KEY = settings.UNSPLASH_API_KEY
BASE_URL = "https://api.unsplash.com"

def generate_image(term): 
    response = requests.get(f"{BASE_URL}/search/photos", params={"query": term, "per_page": 1}, headers={"Authorization": f"Client-ID {API_KEY}"})
    data = response.json()
    thumb_nail = data["results"][0]["urls"]["thumb"]
    full_image = data["results"][0]["urls"]["full"]

    return {"image_name": term, "thumbnail": thumb_nail, "full_image": full_image}
