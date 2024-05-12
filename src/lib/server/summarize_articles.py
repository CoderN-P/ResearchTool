from .get_google_articles import get_google_articles
from .summarize import summarize


def summarize_articles(query):
    articles = get_google_articles(query)
    return [summarize(article) for article in articles]