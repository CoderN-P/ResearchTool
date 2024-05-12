import newspaper

from src.lib.server.get_google_articles import get_google_articles


def summarize(article_obj):
    try:
        article = newspaper.article(article_obj["url"])
        article.download()
        article.parse()
        article.nlp()

        return {"summary": article.summary, "keywords": article.keywords, "authors": article.authors, "publish_date": article.publish_date, "url": article_obj["url"], "title": article_obj["title"]}
    except: # noqa
        return "Failed to summarize article"

