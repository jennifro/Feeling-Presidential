import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import json

#############################################
with open('positive-speech.json') as pluses:
    info1 = json.load(pluses)

with open('negative-speech.json') as minuses:
    info2 = json.load(minuses)

# info1 & 2 are lists of dictionaries.


def training_corpora(texts):
    """Returns a list of lists containing individual words from a json file."""

    return [item['TEXT'].split() for item in texts]


def bag_o_words(words):
    """Return bag of words from a list of strings."""

    return dict([(w, True) for word in words for w in word])


posdata = training_corpora(info1)
negdata = training_corpora(info2)

posfeats = [(bag_o_words(text), 'pos') for text in posdata]
negfeats = [(bag_o_words(text), 'neg') for text in negdata]

poscut = len(posfeats)*3/4
negcut = len(negfeats)*3/4

trainfeats = posfeats[:poscut] + negfeats[:negcut]
testfeats = posfeats[poscut:] + negfeats[negcut:]

print 'train on %d words, test on %d words' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()
