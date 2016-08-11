from speechinfo import get_speech_text
from collection import defaultdict
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

#############################################
# IMPORT THE LIST OF ALL SPEECH TEXTS HERE!!

def speech_feats(all_speeches):
    all_speeches = ''.join(get_speech_text())

    return dict([(word, True) for word in )


def evaluate_classifier():
    # trainer = .67 * len(allspeeches)
    # tester = .33 * len(allspeeches)

    # make a random # of allspeches the trainer set
    # same with tester

print 'train on %d speeches, test on %d speeches' % (len(trainer), len(tester))

classifer = NaiveBayesClassifier.train(trainer)
print 'accuracy:', nltk.classify.util.accuracy(classifier, tester)
classifier.show_most_informative_features()    
