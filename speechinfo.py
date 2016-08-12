import json
import string


def get_speech_text():
    """Returns a list of all speeches from scrapy json file."""
    # Make a test here with a different file maybe?

    data = open('allspeeches.json')

    all_speech_info = json.load(data)

    full_corpora = []
    excess = string.whitespace
    clean_spaces = string.maketrans(excess, ' '*len(excess))

    for x in range(len(all_speech_info)):
        text = (''.join(all_speech_info[x]['speech'])).encode('ascii', 'ignore').lower()
        text = text.translate(clean_spaces)
        text = text.split()

        full_corpora.append(text)

    return full_corpora


def get_speech_info():
    """ """
    pass
