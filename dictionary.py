import re
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')

# Handles removal of redundant/repeat words
def removeDuplicateWords(tok):
    i = 0
    tok2 = tok
    tok3 = tok2
    for i in range(len(tok)-1):
        if tok[i] != tok2[i+1]:
            tok3[i] = tok[i]
            tok3[i+1] = tok2[i+1]
        elif tok[i] == tok2[i+1]:
            tok3[i] = tok[i]
            tok3[i+1] = " "
    fixedd = tok3
    return fixedd

# Handles removal of repeat sentences
# Isolates sentence using a regular expression which identifies the end of a sentence by a full stop or
# punctuation followed by a capital letter. Then compares and removes the first instance.
def removeDuplicatePhrase(txt):
    text = re.sub(r'((\b\w+\b.{1,2}\w+\b)+).+\1', r'\1', txt, flags=re.I)
    return text

# Main tokenizer function which calls and handles all other functions
def Tokenizer(txt):
    # tokenizes and indexes the inputted string
    tokens = nltk.word_tokenize(txt)
    i = 0
    # First stage of Correcting misspelt words, Changes abbreviations to their extended form
    # Fix spelling mistakes
    # And replaces specified words or phrases
    # handles specified colloquial language (Jamaican patois) if specified
    for i, val in enumerate(tokens):
        if tokens[i] == "You":
            if tokens[i + 1] == "ve":
                tokens[i] = "You"
                tokens[i + 1] = "have"
        if tokens[i] == "I":
            if tokens[i + 1] == "ve":
                tokens[i] = "I"
                tokens[i + 1] = "have"
        if tokens[i] == "wasn":
            if tokens[i + 1] == "t":
                tokens[i] = "was"
                tokens[i + 1] = "not"
        if tokens[i] == "they":
            if tokens[i + 1] == "re":
                tokens[i] = "they"
                tokens[i + 1] = "are"
        if tokens[i] == "I":
            if tokens[i + 1] == "m":
                tokens[i] = "I"
                tokens[i + 1] = "am"
        if tokens[i] == "wil":
            tokens[i] = "will"
        if tokens[i] == "bby":
            tokens[i] = "baby"
        if tokens[i] == "ar":
            tokens[i] = "are"
        if tokens[i] == "cn":
            tokens[i] = "can"
        if tokens[i] == "grl":
            tokens[i] = "girl"
        if tokens[i] == "rd":
            tokens[i] = "road"
        if tokens[i] == "st":
            tokens[i] = "street"
        if tokens[i] == "ty":
            tokens[i] = "thank you"
        if tokens[i] == "minuets":
            tokens[i] = "minutes"
        if tokens[i] == "thi":
            tokens[i] = "this"
        if tokens[i] == "yu":
            tokens[i] = "you"
        if tokens[i] == "ws":
            tokens[i] = "was"
        if tokens[i] == "t":
            tokens[i] = "to"
        if tokens[i] == "th":
            tokens[i] = "the"
        if tokens[i] == "yte":
            tokens[i] = "yet"
        if tokens[i] == "nce":
            tokens[i] = "nice"
        if tokens[i] == "corect":
            tokens[i] = "correct"
        if tokens[i] == "atm":
            tokens[i] = "at the moment"
        if tokens[i] == "aka":
            tokens[i] = "also known as"
        if tokens[i] == "btw":
            tokens[i] = "by the way"
        if tokens[i] == "asap":
            tokens[i] = "as soon as possible"

        # After changes are made, passes tokenized string to tokfix function for removal of duplicate words
    tokfix = removeDuplicateWords(tokens)
    # String from tokfix is passed back to this function into the detokenizer and initialised into the output variable
    output = TreebankWordDetokenizer().detokenize(tokfix)
    # output string is passed into the remove duplicate phrases function, to remove duplicate sentences
    result = removeDuplicatePhrase(output)

    print(result)
    return result
