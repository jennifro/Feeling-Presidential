import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
# from nltk.classify.scikitlearn import SklearnClassifier
# from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from nltk.collocations import *
import nltk.metrics
import json
from utilities import str_parser
import random

#############################################
with open('positive-speech.json') as pluses:
    info1 = json.load(pluses)

with open('negative-speech.json') as minuses:
    info2 = json.load(minuses)

with open('allspeeches.json') as speeches:
    real_data = json.load(speeches)


# pickle classifier?

def training_corpora(texts):
    """Returns a list of lists containing individual words from json file."""

    full_speeches = []

    for item in texts:
        original_text = item['TEXT']
        speech = str_parser(original_text)

        full_speeches.append(speech)

    return full_speeches

# makes 1 giant list of individual speech text as lists divided into words
posdata = training_corpora(info1)
negdata = training_corpora(info2)

random.shuffle(posdata)
random.shuffle(negdata)

# finding the most common words in all speeches
all_words = []

for item in posdata:
    for word in item:
        all_words.append(word)

for item in negdata:
    for word in item:
        all_words.append(word)


most_common = nltk.FreqDist(all_words)

common_feats = list(most_common.keys())[:1500]


def get_features(document):

    words = set(document)
    features = {}
    for word in common_feats:
        features[word] = (word in words)

    return features


# creates list of tuples: [ ({word: True}, pos/neg), (), () ]
pos_tags = [(get_features(speech), 'pos') for speech in posdata]
neg_tags = [(get_features(speech), 'neg') for speech in negdata]


poscut = len(pos_tags)*7/8
negcut = len(neg_tags)*7/8

trainfeats = pos_tags[:poscut] + neg_tags[:negcut]
testfeats = pos_tags[poscut:] + neg_tags[negcut:]

print 'training on %d texts, testing on %d texts' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features(15)

# MNB_classifier = SklearnClassifier(MultinomialNB())
# MNB_classifier.train(trainfeats)
# print("MNB_classifier accuracy:", (nltk.classify.accuracy(MNB_classifier, testfeats)))

# BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
# BernoulliNB_classifier.train(trainfeats)
# print("BernoulliNB_classifier accuracy:", (nltk.classify.accuracy(BernoulliNB_classifier, testfeats)))


def analyze_speeches():
    """Sentiment analysis on presidential speeches."""

    sentiment_scores = {}

    for data in real_data:
        title = ''.join(data['title'])          # returns string value of title
        text_string = ''.join(data['TEXT'])

        speech = str_parser(text_string)

        speech = get_features(speech)

        sentiment = classifier.classify(speech)

        sentiment_scores[title] = sentiment

    return sentiment_scores

###### old code ########

# pos_words = []

# for item in posdata:
#     for word in item:
#         pos_words.append(word)

# neg_words = []

# for item in negdata:
#     for word in item:
#         neg_words.append(word)

# pos_words = nltk.FreqDist(pos_words)
# neg_words = nltk.FreqDist(neg_words)

# pos_features = list(pos_words.keys())[:1500]
# neg_features = list(neg_words.keys())[:1500]


# def bag_o_words(words):
#     """Return bag of words from a list of strings."""

#     return dict([(word, True) for word in words])
