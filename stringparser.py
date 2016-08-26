import regex as re
from nltk.corpus import stopwords

excess = stopwords.words('english')


def str_parser(sentence):
    """Takes a unicode string of any length, returns string as a list
    split into lowercase words without punctuation."""

    all_lower = sentence.lower()

    clean_text = re.sub(r'\p{P}', '', all_lower)  # removes punctuatation from unicode

    indiv_words = clean_text.split()

    for word in excess:
        while word in indiv_words:
            indiv_words.remove(word)         # removes words like 'and', 'the', 'or'

    return indiv_words
