import sys 
sys.path.append('src/iterations')

from first_image_detector import ImageDetector
import unittest
import random
import json

class TestImageDetector(unittest.TestCase):

    '''
    This function sets up the image detector object. It runs every test is performed
    '''

    def setUp(self):
        self.image_detector = ImageDetector(image_url="https://images.pexels.com/photos/378570/pexels-photo-378570.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500")

    '''
    This function tests the image labelling
    '''
    def test_get_image_labels(self):
        ex_labels = ["building", "town", "people", "traffic", "cityscape", "infrastructure", "city", "skycrapper", "downtown"]
        labels = self.image_detector.get_image_labels()
        # labels = [label["description"] for label in labels]
        self.assertEqual(ex_labels, labels)

    '''
    This function tests the object detection
    '''

    def test_get_image_objects(self):
        ex_objects = ["person", "flag", "car"]
        objects = self.image_detector.get_image_objects()
        # objects = [obj["name"] for obj in objects]
        self.assertEqual(ex_objects, objects)

if __name__ == "__main__":
    unittest.main()
