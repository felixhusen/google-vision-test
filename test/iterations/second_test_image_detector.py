import sys 
sys.path.append('src/iterations')

from second_image_detector import ImageDetector
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
        labels = [label["description"] for label in labels]
        score = self.score_comparison(ex_list=ex_labels, ac_list=labels)
        # Print results
        print("Test Description: Labelling Test")
        print("Description: ", labels["description"])
        print("Similarity Score: ", score)
        # Test will pass if the similarity score > 0.1
        self.assertGreaterEqual(score, 0.1)

    '''
    This function tests the object detection
    '''

    def test_get_image_objects(self):
        ex_objects = ["person", "flag", "car"]
        objects = self.image_detector.get_image_objects()
        objects = [obj["name"] for obj in objects]
        score = self.score_comparison(ex_list=ex_objects, ac_list=objects)
        # Print results
        print("Test Description: Labelling Test")
        print("Description: ", objects["name"])
        print("Similarity Score: ", score)
        # Test will pass if the similarity score > 0.1
        self.assertGreaterEqual(score, 0.1)


    def score_comparison(self, ex_list, ac_list):
        # Remove duplicates
        ex_list = list(dict.fromkeys(ex_list))
        ac_list = list(dict.fromkeys(ac_list))
        # Initialise correct count
        correct_count = 0
        # Make all the string to lower
        ac_list = [ac_item.lower() for ac_item in ac_list]
        # Count the correct item
        for ex_item in ex_list:
            if ex_item.lower() in ac_list:
                correct_count += 1
        # Measure the score
        score = correct_count / len(ac_list)
        return score

if __name__ == "__main__":
    unittest.main()
