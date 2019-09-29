import urllib.request,json
from .models import Quotes
import requests
from config import Config

base_url = Config.QUOTE_URL


def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    quote_object = requests.get(base_url)
    new_quote=quote_object.json()
    quote = new_quote.get('quote')
    author = new_quote.get('author')
    quote_object = Quotes(quote,author)
        

    return quote_object
    