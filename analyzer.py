from speechinfo import get_speech_text
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

#############################################
# MOST OF THIS IS TRASH PROBABLY, MAYBE, WE'LL SEE

all_speeches = get_speech_text()  # list of strings
big_string = (''.join(all_speeches)).split()


def bag_o_words(words):
    """Return bag of words from a list of strings."""

    return dict([(word, True) for word in words])

speech_corpus = (bag_o_words(big_string))
trainer_cut = len(speech_corpus)*2/3


#### this needs to be a dictionary #####
trainer = big_string[:trainer_cut]
tester = big_string[trainer_cut:]

print 'train on %d words, test on %d words' % (len(trainer), len(tester))

classifier = NaiveBayesClassifier.train(trainer)
print 'accuracy:', nltk.classify.util.accuracy(classifier, tester)
classifier.show_most_informative_features()
