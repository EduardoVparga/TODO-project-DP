import requests

from src.images.animal_request import (
    AnimalAPI
)
# Adapter for the dog API
class DogAPIAdapter(AnimalAPI):
    def __init__(self):
        self.url = "https://dog.ceo/api/breeds/image/random"

    def get_animal_image(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data["message"]
        else:
            return None