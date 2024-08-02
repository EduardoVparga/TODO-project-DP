import unittest
from unittest.mock import patch

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.images.cat import CatAPIAdapter
from src.images.dog import DogAPIAdapter
from src.images.animal_request import AnimalClient, AnimalAPI

class TestCatAPIAdapter(unittest.TestCase):
    @patch('src.images.cat.requests.get')
    def test_get_animal_image_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [{"url": "http://example.com/cat.jpg"}]
        
        adapter = CatAPIAdapter()
        image_url = adapter.get_animal_image()
        self.assertEqual(image_url, "http://example.com/cat.jpg")
        
    @patch('src.images.cat.requests.get')
    def test_get_animal_image_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        
        adapter = CatAPIAdapter()
        image_url = adapter.get_animal_image()
        self.assertIsNone(image_url)

class TestDogAPIAdapter(unittest.TestCase):
    @patch('src.images.dog.requests.get')
    def test_get_animal_image_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "http://example.com/dog.jpg"}
        
        adapter = DogAPIAdapter()
        image_url = adapter.get_animal_image()
        self.assertEqual(image_url, "http://example.com/dog.jpg")
        
    @patch('src.images.dog.requests.get')
    def test_get_animal_image_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        
        adapter = DogAPIAdapter()
        image_url = adapter.get_animal_image()
        self.assertIsNone(image_url)

class TestAnimalClient(unittest.TestCase):
    @patch('src.images.animal_request.random.choice')
    def test_show_animal_image_success(self, mock_choice):
        mock_api = unittest.mock.Mock(spec=AnimalAPI)
        mock_api.get_animal_image.return_value = "http://example.com/animal.jpg"
        mock_choice.return_value = mock_api
        
        client = AnimalClient([mock_api])
        image_url = client.show_animal_image()
        self.assertEqual(image_url, "http://example.com/animal.jpg")
        
    @patch('src.images.animal_request.random.choice')
    def test_show_animal_image_failure(self, mock_choice):
        mock_api = unittest.mock.Mock(spec=AnimalAPI)
        mock_api.get_animal_image.return_value = None
        mock_choice.return_value = mock_api
        
        client = AnimalClient([mock_api])
        image_url = client.show_animal_image()
        self.assertIsNone(image_url)

if __name__ == '__main__':
    unittest.main()
