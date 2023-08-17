import requests

google_books_endpoint = 'https://www.googleapis.com/books/v1/volumes'
API_KEY = 'AIzaSyChVvbQvSXosrxSsR8BoqtRPUzldldkyH0'


def get_book_info(query):
    params = {
        'q': query,
        'key': API_KEY
    }
    request = requests.get(google_books_endpoint, params=params)
    response = request.json()
    data = response['items'][0]['volumeInfo']
    description = data['description']
    published_date = data['publishedDate']
    page_count = data['pageCount']
    average_rating = data.get('averageRating', 0.0)
    return description, published_date, page_count, average_rating

