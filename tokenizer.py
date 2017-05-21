import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')

custom_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_tokenizer.tokenize(sample_text)

print tokenized

def process_tokenized():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            # RB: any tense adverb, VB: any tense verb, NN: any noun
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<FW>+}
                                    }<VB.?|IN|DT|TO>+{"""
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            print(chunked)

            for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
                print subtree

    except Exception as e:
        print str(e)

process_tokenized()