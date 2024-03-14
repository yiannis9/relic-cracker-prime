import requests
from dataclasses import dataclass
from typing import List
from keras_ocr import tools
from keras_ocr.pipeline import Pipeline

class WFMCaller:
    
    def __init__(self):
        self.url = 'https://api.warframe.market/v1'
    
    def get_item(self, item: str):
        
        headers = {
            'accept': 'application/json',
            'Accept-Language': 'en',
            'platform': 'pc',
        }
        
        response = requests.get(self.url+f'/items/{item}')
              
        return response.json()


class ModelWrapper:
    
    def __init__(self):
        self.pipeline = Pipeline()
        
            
    def get_results(self, img):
        results = self.pipeline.recognize([img])
        for result in results:
            print(f'BBox: {result["bounding_box"]}, Text: {result["text"]}')
        
        return results

@dataclass
class Item:
    name: str
    url_name: str
    id: str
    item_type: str
    rarity: str
    tags: List[str]
    thumb: str
    ducats: int
    plat: int

    