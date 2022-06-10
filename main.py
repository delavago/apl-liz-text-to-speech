#imported packages used 
import numpy as np
import array as arr
from tkinter import *
from tkinter import filedialog
import pyttsx3
from tika import parser
import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('tagsets')

import re
import PyPDF2 
# import fitz
from gingerit.gingerit import GingerIt
import streamlit as st

#Text to speech function
def TextToSpeech(txt):
    engine = pyttsx3.init()
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[0].id)
#     engine.setProperty('rate', 150)
    engine.say(txt)
    engine.runAndWait()
    engine.stop()

#Text to Speech PDF Function
def TextToSpeechPdf(doc):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    raw = parser.from_file(doc)
    engine.say(raw['content'])
    engine.runAndWait()

#Handles removal of redundant/repeat words
def tokenfix(tok):
        i = 0
        parser = GingerIt()
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

#Handles removal of repeat sentences
#Isolates sentence using a regular expression which identifies the end of a sentence by a full stop or 
#punctuation followed by a capital letter. Then compares and removes the first instance.
def removeDuplicatePhrase(txt):
        text = re.sub(r'((\b\w+\b.{1,2}\w+\b)+).+\1', r'\1', txt, flags =re.I)
        return text

#Main tokenizer function which calls and handles all other functions
def Tokenizer(txt):
#tokenizes and indexes the inputted string
    tokens = nltk.word_tokenize(txt)
    i = 0
    #First stage of Correcting misspelt words, Changes abbreviations to their extended form
    #Fix spelling mistakes 
    #And replaces specified words or phrases
    #handles specified colloquial language (Jamaican patois) if specified 
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

        #After changes are made, passes tokenized string to tokfix function for removal of duplicate words
    tokfix = tokenfix(tokens)
        #String from tokfix is passed back to this function into the detokenizer and initialised into the output variable
    output = TreebankWordDetokenizer().detokenize(tokfix)
        #output string is passed into the remove duplicate phrases function, to remove duplicate sentences
    result = removeDuplicatePhrase(output)
        #The gingerIt module is called and the result variable is passed into the parser.parse function
        #to fix any additional misspelt words, grammatical errors, redundant punctuation that wasnt originally 
        #specified within the IF Block of code aformentioned earlier in the tokenizer function
    parser = GingerIt()
        #result is passed into another variable after the fixes to be outputted
    val = parser.parse(result)
    print(val)
    print(val["result"])
    #specific result output is captured passed into a second variable
    val2 = val["result"]
    #final corrected text is returned and passed to its appropriate text to speech engine. (whether pdf, txt, or plain text)
    return val2








#Tkinter button to handle plain text entered within the textarea
def submit():
    input1 = textbox.get("1.0","end-1c")
    #function call to plain text text to speech engine
    TextToSpeech(Tokenizer(input1))

#Tkinter button to handle selection of text files from host computer
def txtsubmit():
    root.filename = filedialog.askopenfilename(initialdir='', title="Select file", filetypes=(("txt files","*.txt"),("all files", "*.*")))
    raw = parser.from_file(root.filename)
    #function call to text files text to speech engine
    TextToSpeech(Tokenizer(raw['content']))
    
#Tkinter button to handle selection of pdf files from host computer 
def pdfsubmit():
    pdfdoc = filedialog.askopenfilename(initialdir='', title="Select file", filetypes=(("pdf files","*.pdf"),("all files", "*.*")))
    with fitz.open(pdfdoc) as doc:
        text=""
        for page in doc:
            text +=page.getText() 
#function call to pdf files text to speech engine
    TextToSpeech(Tokenizer(text))

root = Tk()
root.title('Text to Speech')
root.iconbitmap('logo.ico')
root.geometry("500x500")

textbox = Text(root, width = 50, height = 3, fg = 'red')
textbox.pack()

b1 = Button(root, text = "Text to Speech", padx=5, pady=5, bg='white', fg='green', command=submit)
b1.pack()

b2 = Button(root, text = "Open Text File", padx=5, pady=5, bg='white', fg='green', command=txtsubmit)
b2.pack()

b3 = Button(root, text = "Open PDF File", padx=5, pady=5, bg='white', fg='green', command=pdfsubmit)
b3.pack()

root.mainloop()

