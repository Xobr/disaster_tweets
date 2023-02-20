import re
from toolz import pipe

urls_regex = r'http\S+'
mentions_regex = r'@\S+'
hashtags_regex = r'#\S+'


def remove_urls(text):
    return re.sub(urls_regex, '', text)


def remove_mentions(text):
    return re.sub(mentions_regex, '', text)


def remove_hashtags(text):
    return re.sub(hashtags_regex, '', text)


def clean_text(text):
    return pipe(text,
                remove_urls,
                remove_mentions,
                remove_hashtags,
                str.strip)
