import requests
import json
import argparse

class ImageDetector():

    GOOGLE_VISION_API_URL = "https://vision.googleapis.com/v1/images:annotate?key=XXXX"

    '''
    This function initialises the class with the parameter of image url
    '''
    def __init__(self, image_url=""):
        self.image_url = image_url

    '''
    This function will analyse and label the image
    '''

    def get_image_labels(self, max_results=10):
        pass

    '''
    This function will analyse and detect objects in the image
    '''


    def get_image_objects(self, max_results=10):
        pass

    '''
    This function will set the url of the image analysed
    '''
    def set_image_url(self, image_url):
        pass