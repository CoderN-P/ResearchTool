from get_google_articles import get_google_articles
from summarize import summarize


def summarize_articles(query):
    articles = get_google_articles(query)
    results = [summarize(article) for article in articles]
    return [r for r in results if isinstance(r, dict)]
