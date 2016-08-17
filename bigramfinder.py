import nltk
from nltk.collocations import *
from nltk.corpus import stopwords
import json

with open('allspeeches.json') as speeches:
    real_data = json.load(speeches)

extra_words = stopwords.words('english')

others = ['united', 'states', 'american', '.', 'white house', 'i', 'we', 'us',
          'you', 'he', 'she', 'him', 'it', 'they', 'them', 'its']

others = [word.decode(errors='strict') for word in others]

extra_words.extend(others)

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

######### get bigrams ##############

        speech = ''.join(data['TEXT']).lower().split()

        for word in speech:
            if word in extra_words:
                speech.remove(word)

        finder = BigramCollocationFinder.from_words(speech)

        finder.apply_freq_filter(3)

        ngrams = finder.nbest(bigram_measures.pmi, 5)  # list of tuples

        prez_phrases[prez_name][title] = ngrams

    return prez_phrases
