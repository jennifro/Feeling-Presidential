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
    """Returns a list of lists containing individual words from a json file."""

    speech = [item['TEXT'].split() for item in texts]

    for word in extra_words:
        while word in speech:
            speech.remove(word)

    return speech


def bag_o_words(words):
    """Return bag of words from a list of strings."""

    return dict([(word.lower(), True) for word in words])


posdata = training_corpora(info1)
negdata = training_corpora(info2)

posfeats = [(bag_o_words(text), 'pos') for text in posdata]
negfeats = [(bag_o_words(text), 'neg') for text in negdata]

poscut = len(posfeats)*3/4
negcut = len(negfeats)*3/4

trainfeats = posfeats[:poscut] + negfeats[:negcut]
testfeats = posfeats[poscut:] + negfeats[negcut:]

# look for sentimental words already tagged
# look for newspaper articles that are 'mostly' positive or negative
# try with non-political data, maybe social media
# label top 50 bigrams across all speeches
# run bigrams through

print 'train on %d texts, test on %d texts' % (len(trainfeats), len(testfeats))

classifier = NaiveBayesClassifier.train(trainfeats)
print 'accuracy:', nltk.classify.util.accuracy(classifier, testfeats)
classifier.show_most_informative_features()


for data in real_data:
    print 'Testing on', data['title'], 'by', data['president']
    speech = ''.join(data['TEXT']).split()
    for word in speech:
        if word in extra_words:
            speech.remove(word)
    speech = bag_o_words(speech)

    print classifier.classify(speech)

# Need output I can put in speechinfo
# write function to call info and then call function in speechinfo.py
