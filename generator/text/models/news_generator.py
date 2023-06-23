from newsapi import NewsApiClient

my_api_key = '10f27a32c3224f959563a9964bbd70db'

newsapi = NewsApiClient(api_key=my_api_key)


def top_news(category, language='en', query=None, sources=None):

    if sources is not None:
        top_headlines = newsapi.get_top_headlines(q=query,
                                                  sources=sources,
                                                  language=language)
    else:
        top_headlines = newsapi.get_top_headlines(q=query,
                                                  category=category,
                                                  language=language)

    return top_headlines