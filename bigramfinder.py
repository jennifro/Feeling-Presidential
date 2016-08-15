import nltk
from nltk.collocations import *
from nltk.corpus import stopwords
from speechinfo import get_speech_text

allspeeches = get_speech_text()


def remove_stopwords(text):

    extra_words = stopwords.words('english')
    extra_words.extend(['united', 'states'])

    for word in text:
        if word in extra_words:
            text = text.remove(word)
    return text

#### NEED TO ID EACH PRESIDENT WITH THEIR SPEECH!

bigram_measures = nltk.collocations.BigramAssocMeasures()

for speech in allspeeches:

    speech = remove_stopwords(speech)

    finder = BigramCollocationFinder.from_words(speech)

    finder.apply_freq_filter(3)

    print finder.nbest(bigram_measures.pmi, 3)
