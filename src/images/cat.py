import requests

from src.images.animal_request import (
    AnimalAPI
)

# Adapter for the cat API
class CatAPIAdapter(AnimalAPI):
    def __init__(self):
        self.url = "https://api.thecatapi.com/v1/images/search?limit=1"

    def get_animal_image(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data[0]["url"]
        else:
            return None

