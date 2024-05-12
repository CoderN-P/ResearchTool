from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

custom_search = build('customsearch', 'v1', developerKey=os.environ['GOOGLE_API_KEY'])


def get_google_articles(query):
    data = custom_search.cse().list(q=query, cx=os.environ['GOOGLE_SEARCH_ENGINE_ID']).execute()['items']
    return [{"url": item['link'], "title": item['title']} for item in data]


