# 01/05/2017

# Does not implement a very robust SBD system at this moment.
# An improvement would be to follow Wikipedia's "vanilla" approach of
# using a hand-compiled list of abreviations but I was unable to find a good one.
# https://en.wikipedia.org/wiki/Sentence_boundary_disambiguation
#
# Does not group singular/plural words, e.g.: car and cars

import re

with open(r"..\\..\\other\\en_stopwords.txt", "r") as f_stops:
    STOP_WORDS = {word.rstrip() for word in f_stops.readlines()}

def tokenize_sentence(sentence):
    '''Creates a list of words from a sentence'''
    return [re.sub(r"\W+", "", word) for word in sentence.split()]

def create_bag_of_words(sentences):
    '''Returns a bag of words and their frequency'''
    bag = {}
    for s in sentences:
        for word in tokenize_sentence(s):
            word = word.lower()
            if word in bag:
                bag[word] += 1
            elif word not in STOP_WORDS:
                bag[word] = 1
    return bag

def score_sentence(sentence, bag):
    '''Scores a sentence based on the presence of words from the bag provided'''
    sentence = [x.lower() for x in tokenize_sentence(sentence)]
    return sum([1 for w in bag if w in sentence])

def summarize_text(filename="text.txt", n_top_words=4, n_sentences=2):
    with open(filename, "r") as f_text:
        text = re.sub(r"\n(?=\w)", " ", f_text.read())
        sentences = [s.rstrip() for s in re.split(r"(?<=[\.!?]) ", text)]

    bag = create_bag_of_words(sentences)
    top_words = sorted(bag, key=bag.get, reverse=True)[0:n_top_words]

    ranked = {k: v for k, v in zip(sentences, [score_sentence(s, top_words) for s in sentences])}
    summary_sentences = sorted(ranked, key=ranked.get, reverse=True)[0:n_sentences]

    return ' '.join(sorted(summary_sentences, key=sentences.index))

if __name__ == "__main__":
    print(summarize_text())
