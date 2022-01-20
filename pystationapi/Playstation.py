import json
import urllib.request
import urllib.parse
import logging
import hashlib
from datetime import date
from pystationapi import PlaystationObject

logging.basicConfig(filename="./log/playstation.log", level= logging.DEBUG)

class Playstation:
    language = ""
    BASE_URL =  "https://web.np.playstation.com/api/graphql/v1/op"
    PS4_GAMES = '44d8bb20-653e-431e-8ad0-c0a365f68d2f'
    PS5_GAMES = '4cbf39e2-5749-4970-ba81-93a489e4570c'
    PS_PLUS = '038b4df3-bb4c-48f8-8290-3feb35f0f0fd'
    SALES = '803cee19-e5a1-4d59-a463-0b6b2701bf7c'
    EA_GAMES = '74d4e266-5c64-4c61-a7e3-1b6e78f643e6'
    sha256hash = '"4ce7d410a4db2c8b635a48c1dcec375906ff63b19dadd87e073f8fd0c0481d35'
    LANGUAGE = "it-IT"
    BASE_URL_STORE = "https://store.playstation.com/it-it/product/"
    

    def to_json_from_category(self,category,pagination):
        responsePlaystation = self.componi_url(category,pagination)
        responselist = []
        for playstationElement in responsePlaystation.get('data').get('categoryGridRetrieve').get('products'):
            playstation = PlaystationObject(
                playstationElement.get('id'),
                playstationElement.get('price').get('discountText'),
                [ x.get('url') for x in playstationElement.get('media') ],
                playstationElement.get('name'),
                self.BASE_URL_STORE+playstationElement.get('id'),
                playstationElement.get('price').get('basePrice'),
                playstationElement.get('price').get('discountedPrice'),
                None,
                None,
                str(date.today()),
                "Playstation",
                hashlib.sha256(json.dumps(playstation).encode('utf8')).hexdigest()
            )
            
            responselist.append(playstation)
        return json.dumps(responselist)

    
    def componi_url(self,category,pagination):
        
        new_params = {'operationName':'categoryGridRetrieve', 
                       'variables': 
                                    {
                                        "id":category,
                                        "pageArgs":
                                                {
                                                    "size":pagination,
                                                    "offset":0
                                                },
                                                "sortBy":null,
                                                "filterBy":[],
                                                "facetOptions":[]
                                    },
                                    'extensions':
                                            {
                                                "persistedQuery":
                                                {
                                                    "version":1,
                                                    "sha256Hash":"4ce7d410a4db2c8b635a48c1dcec375906ff63b19dadd87e073f8fd0c0481d35"
                                                }
                                            }
                    }
        new_params_encoded = urllib.urlencode(new_params)
        
        request = urllib.request.Request(self.BASE_URL,data=new_params_encoded)
        request.add_header("x-psn-store-locale-override",self.LANGUAGE)
        response = json.loads(urllib.request.urlopen(request).read().decode())
        return response

    def insert_in_mongo(self,dbconnection_collection,playstationObject):
        responsefromweb = self.to_json_from_category(self.SALES,340)
        dbconnection_collection.insert_one(playstationObject)