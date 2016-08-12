import nltk
from nltk.collocations import *
from speechinfo import get_speech_text

allspeeches = get_speech_text()

#### NEED TO ID EACH PRESIDENT WITH THEIR SPEECH!

bigram_measures = nltk.collocations.BigramAssocMeasures()

for speech in allspeeches:

    finder = BigramCollocationFinder.from_words(speech)

    # remove stopwords here?

    finder.apply_freq_filter(3)

    print finder.nbest(bigram_measures.pmi, 3)
