import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
# from nltk.classify.scikitlearn import SklearnClassifier
# from sklearn.naive_bayes import MultinomialNB, BernoulliNB
import collections
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import *
import json
import itertools
from utilities import str_parser
import pickle
# import random

#############################################
with open('positive-speech.json') as pluses:
    info1 = json.load(pluses)

with open('negative-speech.json') as minuses:
    info2 = json.load(minuses)


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

# random.shuffle(posdata)
# random.shuffle(negdata)

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
    """Returns feature dictionary given an object with single-word elements.

    Output is a dictionary where a word appearing a list object is the key,
    and a boolean (True) as the value.
    """

    words = set(document)
    features = {}
    for word in common_feats:
        features[word] = (word in words)

    return features


def bigram_features(words, score_fn=BigramAssocMeasures.chi_sq, n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return dict([(ngram, True) for ngram in itertools.chain(words, bigrams)])


# pickle classifier?

"""Code below determines overall positivity or negativity for a political text.

Uses a Naive Bayes Classifier trained on around 50 American political speeches
from 1960-2016.

Because it uses data that is shuffled every time the file is ran, the output
of most informative features will vary slightly. Expected accuracy is ~62%.
"""

pos_tags = [(get_features(speech), 'pos') for speech in posdata]
neg_tags = [(get_features(speech), 'neg') for speech in negdata]

poscut = len(pos_tags)*7/8
negcut = len(neg_tags)*7/8

trainfeats = pos_tags[:poscut] + neg_tags[:negcut]
testfeats = pos_tags[poscut:] + neg_tags[negcut:]

print 'training on %d texts, testing on %d texts' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats)

save_classifier = open('naivebayes.pickle', "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

testsets = collections.defaultdict(set)
refsets = collections.defaultdict(set)

for i, (feats, label) in enumerate(testfeats):
    refsets[label].add(i)
    observed = classifier.classify(feats)
    testsets[observed].add(i)

print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
print 'pos precision:', precision(refsets['pos'], testsets['pos'])
print 'pos recall:', recall(refsets['pos'], testsets['pos'])
print 'neg precision:', precision(refsets['neg'], testsets['neg'])
print 'neg recall:', recall(refsets['neg'], testsets['neg'])
classifier.show_most_informative_features(15)

# MNB_classifier = SklearnClassifier(MultinomialNB())
# MNB_classifier.train(trainfeats)
# print("MNB_classifier accuracy:", (nltk.classify.accuracy(MNB_classifier, testfeats)))

# BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
# BernoulliNB_classifier.train(trainfeats)
# print("BernoulliNB_classifier accuracy:", (nltk.classify.accuracy(BernoulliNB_classifier, testfeats)))

with open('allspeeches.json') as speeches:
    real_data = json.load(speeches)


def analyze_speeches():
    """Sentiment analysis on presidential speeches."""

    sentiment_scores = {}

    for data in real_data:
        title = ''.join(data['title'])          # returns string value of title
        text_string = ''.join(data['TEXT'])

        speech = str_parser(text_string)

        speech_feats = get_features(speech)

        sentiment = classifier.classify(speech_feats)

        sentiment_scores[title] = sentiment

    return sentiment_scores
