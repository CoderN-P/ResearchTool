from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ['NEWS_API_KEY'])
# Init
newsapi = NewsApiClient(api_key=os.environ['NEWS_API_KEY'])


def get_articles(q):
    # /v2/everything
    all_articles = newsapi.get_everything(q=q,
                                          from_param='2024-04-12',
                                          to='2024-05-11',
                                          language='en',
                                          sort_by='relevancy')

    return all_articles


print(get_articles('benefits of nuclear energy'))
