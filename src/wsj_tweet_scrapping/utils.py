from nltk.corpus import stopwords
from typing import Dict, List
import re
from pickle import load, dump, HIGHEST_PROTOCOL
from os import mkdir


def dump_pickle(obj, filename: str):
    """Save object in Python pickle form."""
    dump(obj, open(f"{filename}.pickle", "wb"), protocol=HIGHEST_PROTOCOL)


def load_pickle(filename: str):
    """Load Python pickle."""
    if ".pickle" in filename:
        filename = filename.replace(".pickle", "")
    return load(open(f"{filename}.pickle", "rb"))


def create_dir(folder_name: str):
    """
    Create folder if not already exists.

    Assumes folder path is appropriately attached to folder_name.
    """
    try:
        mkdir(folder_name)
    except Exception as e:
        print(f"Failed creating directory, exception : {e}")
    else:
        print("Successfully created directory")


def get_stopwords(lang: str = "english"):
    return stopwords.words(lang)


def find_urls_in_text(text: str) -> List:

    # findall() has been used
    # with valid conditions for urls in string
    regex = (
        r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)"
        "(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()"
        "<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    )
    url = re.findall(regex, text)

    # x[0] because different types of urls will be caught and non-empty type url be at index 0 for every url type caught
    # ex. [('https://www.wsj.com/articles/todays-top-supply-chain-and-logistics-news-from-wsj-1462876696',
    #       '',
    #       '',
    #       '',
    #       ''),
    #      ('http://on.wsj.com/Logisticsnewsletter', '', '', '', '')]
    return [x[0] for x in url]


def get_words_contractions() -> Dict:
    """A list of contractions from
    http://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python"""
    return {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "cannot",
        "can't've": "cannot have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'd've": "he would have",
        "he'll": "he will",
        "he's": "he is",
        "how'd": "how did",
        "how'll": "how will",
        "how's": "how is",
        "i'd": "i would",
        "i'll": "i will",
        "i'm": "i am",
        "i've": "i have",
        "isn't": "is not",
        "it'd": "it would",
        "it'll": "it will",
        "it's": "it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "must've": "must have",
        "mustn't": "must not",
        "needn't": "need not",
        "oughtn't": "ought not",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "she'd": "she would",
        "she'll": "she will",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "that'd": "that would",
        "that's": "that is",
        "there'd": "there had",
        "there's": "there is",
        "they'd": "they would",
        "they'll": "they will",
        "they're": "they are",
        "they've": "they have",
        "wasn't": "was not",
        "we'd": "we would",
        "we'll": "we will",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "where'd": "where did",
        "where's": "where is",
        "who'll": "who will",
        "who's": "who is",
        "won't": "will not",
        "wouldn't": "would not",
        "you'd": "you would",
        "you'll": "you will",
        "you're": "you are",
    }
