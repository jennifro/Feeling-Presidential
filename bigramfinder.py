import nltk
from nltk.collocations import *
import json
from utilities import str_parser

with open('allspeeches.json') as speeches:
    real_data = json.load(speeches)


bigram_measures = nltk.collocations.BigramAssocMeasures()


def top_bigrams():
    """Gets the top 5 bigrams for a speech."""

    prez_phrases = {}

    # dictionary: {prez name: {title: [ (collocation1), (collocation2) ] }}

    for data in real_data:
        # print 'Testing on', data['title'], 'by', data['president']

        prez_name = ''.join(data['president'])

        title = ''.join(data['title'])

        if prez_name not in prez_phrases:
            prez_phrases[prez_name] = {}

        speech_str = ''.join(data['TEXT'])

        speech = str_parser(speech_str)  # returns list of word elements

######### get bigrams ##############

        finder = BigramCollocationFinder.from_words(speech)

        finder.apply_freq_filter(3)

        ngrams = finder.nbest(bigram_measures.pmi, 5)  # list of tuples

        prez_phrases[prez_name][title] = ngrams

    return prez_phrases
