from nytimes import BestSeller
import requests
from lookup import Information




def bestsellingauthors():
    '''
    Gets the current new york times best selling book, for hard-cover fiction books
    Args: None
    '''
    current_best_sellers = BestSeller()
    best_sellers = current_best_sellers.get()
    results = best_sellers['results']['books']
    nytimes_authors = []
    for k, val in enumerate(results): 
        for k, v in val.items():
            if k == 'author':
                nytimes_authors.append(v)
    print(nytimes_authors)
    for k, v in enumerate(nytimes_authors):
        print(v)
        good_books = []
        author_info = Information(v)
        author_info = author_info.get()
        top_works = author_info['docs']
        for k, v in enumerate(top_works): 
            for k, v in v.items():
                if k == 'top_work':
                    good_books.append(v)

        print(good_books)


def main(): 
    bestsellingauthors()

    

main()
