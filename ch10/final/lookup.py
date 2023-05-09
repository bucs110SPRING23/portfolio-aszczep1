import requests


class Information: 

    def __init__(self, author):
         '''
         Initializes in information class 
         Args: self (information object), author (str)
         '''
         self.url = f'https://openlibrary.org/search/authors.json?q={author}&limit=5'

    def get(self):
        '''
        Gets the authors information from API
        Args: self (information object)
        Returns: (str) The authors five best selling books 
        '''
        r = requests.get(f'{self.url}')
        author_info = r.json()
        
        return author_info