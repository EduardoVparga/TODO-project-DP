import random

from src.logger.init import (
    logger,
)

SOURCE = "AnimalAPI Cls"

# Common interface
class AnimalAPI:
    def get_animal_image(self):
        raise NotImplementedError("This method must be implemented by subclasses")


# Client using the common interface
class AnimalClient:
    def __init__(self, apis: AnimalAPI):
        self.apis = apis

    def show_animal_image(self):
        api = random.choice(self.apis)
        image_url = api.get_animal_image()
        if image_url:
            logger.activity(SOURCE, 'INFO', f"Animal image: {image_url}")
            return image_url
            
        else:
            logger.activity(SOURCE, 'WARN', "Could not retrieve the animal image.")
            