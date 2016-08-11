import json
import string


def get_speech_text():
    """Returns a list of all speeches from scrapy json file."""
    # Make a test here with a different file maybe?

    data = open('allspeeches.json')

    all_speech_info = json.load(data)

    # Get all speechtexts as a formatted lower-case ascii string in single list

    full_corpora = []
    excess = string.whitespace
    change = string.maketrans(excess, ' '*len(excess))

    for x in range(len(all_speech_info)):
        text = (''.join(all_speech_info[x]['speech'])).encode('ascii', 'ignore').lower()
        text = text.translate(change)
        text = ' '.join(text.split())

        full_corpora.append(text)

    return full_corpora
