import json
import string

data = open('allspeeches.json')

all_speech_info = json.load(data)


def get_speech_text():
    """Returns a list of all speeches from scrapy json file."""
    # Make a test here with a different file maybe?

    full_corpora = []
    excess = string.whitespace
    clean_spaces = string.maketrans(excess, ' '*len(excess))

    for x in range(len(all_speech_info)):
        text = (''.join(all_speech_info[x]['speech'])).encode('ascii', 'ignore').lower()
        text = text.translate(clean_spaces)
        text = text.split()

        full_corpora.append(text)

    return full_corpora


def get_speech_title():
    """Returns title of speech as a string"""

    for y in range(len(all_speech_info)):
        return ''.join(all_speech_info[y]['title'])


def get_speaker():
    """Returns the president that gave a particular speech"""

    for z in range(len(all_speech_info)):
        return ''.join(all_speech_info[z]['president'])


def get_text_url():
    """ """

    for u in range(len(all_speech_info)):
        return ''.join(all_speech_info[u]['url'])
