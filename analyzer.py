import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import stopwords
from nltk.collocations import *
import nltk.metrics
import json

#############################################
with open('positive-speech.json') as pluses:
    info1 = json.load(pluses)

with open('negative-speech.json') as minuses:
    info2 = json.load(minuses)

with open('allspeeches.json') as speeches:
    real_data = json.load(speeches)

extra_words = stopwords.words('english')


def training_corpora(texts):
    """Returns a list of lists containing individual words from json file."""

    full_speeches = []

    for item in texts:
        speech = item['TEXT'].lower().split()

        for word in extra_words:
            while word in speech:
                speech.remove(word)

        full_speeches.append(speech)

    return full_speeches


def bag_o_words(words):
    """Return bag of words from a list of strings."""

    return dict([(word, True) for word in words])

# wrap this in a function.

posdata = training_corpora(info1)
negdata = training_corpora(info2)

posfeats = [(bag_o_words(text), 'pos') for text in posdata]
negfeats = [(bag_o_words(text), 'neg') for text in negdata]

poscut = len(posfeats)*7/8
negcut = len(negfeats)*7/8

trainfeats = posfeats[:poscut] + negfeats[:negcut]
testfeats = posfeats[poscut:] + negfeats[negcut:]

print 'train on %d texts, test on %d texts' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()


def analyze_speeches():
    """Sentiment analysis on presidential speeches."""

    sentiment_scores = {}

    for data in real_data:
        title = ''.join(data['title'])
        speech = ''.join(data['TEXT']).split()
        for word in extra_words:
            while word in speech:
                speech.remove(word)
        speech = bag_o_words(speech)

        sentiment = classifier.classify(speech)

        sentiment_scores[title] = sentiment

    return sentiment_scores
