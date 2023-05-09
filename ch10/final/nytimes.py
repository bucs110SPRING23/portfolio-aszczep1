import requests
import json

class BestSeller: 

    def __init__(self):
        '''
        Intializes a BestSeller object that will produce a list of best selling new york times authors 
        Args: (BestSeller obj) 
        '''
        self.url = f'https://api.nytimes.com/svc/books/v3/lists/current/hardcover-fiction.json?api-key=1iNf6bA7MfN0ASaHNt59DKCDKARQSnpT'
       

    def get(self):
        '''
        Reads a file from the API that shows the best selling authors
        Args: (BestSeller obj)
        '''
        r = requests.get(f'{self.url}')
        best_seller = r.json()
        
        return best_seller
    

        

        