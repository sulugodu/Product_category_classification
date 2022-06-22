"""Pre-processing pipeline for training."""
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer


def remove_punctuations(description_string):
    """ Remove punctuations."""
    table = str.maketrans('','',string.punctuation)
    return description_string.translate(table)


def pipeline_remove_punctuations(description):
    """Adding pre-processing to sklearn pipeline."""
    return description.apply(remove_punctuations)


def remove_numbers(description_string):
    """Function to emove number."""
    words=re.sub("[^a-zA-Z]"," ",description_string)
    text=words.lower().split()
    return ' '.join(text)


def pipeline_remove_numbers(description):
    """Adding pre-processing to sklearn pipeline."""
    return description.apply(remove_numbers)


stop = stopwords.words(['english','german'])


def remove_stopwords(description_string):
    """The function to removing stopwords"""
    text = [word.lower() for word in description_string.split() if word.lower() not in stop]
    return " ".join(text)


def pipeline_remove_stopwords(description):
    """Adding pre-processing to sklearn pipeline."""
    return description.apply(remove_stopwords)


lem = WordNetLemmatizer()

def word_lem(text):
    """Function to apply lemmatize."""
    lem_text = [lem.lemmatize(word) for word in text.split()]
    return " ".join(lem_text)


def pipeline_word_lem(description):
    """Adding pre-processing to sklearn pipeline."""
    return description.apply(word_lem)


stemmer_porter = PorterStemmer()


def stemmer(description_string):
    """The function to apply stemming"""
    stem_text = [stemmer_porter.stem(word) for word in description_string.split()]
    return " ".join(stem_text)


def pipeline_stemmer(description):
    """Adding pre-processing to sklearn pipeline."""
    return description.apply(stemmer)

