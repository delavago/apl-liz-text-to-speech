#Package imports
import numpy as np
import array as arr
from tkinter import *
from tkinter import filedialog
from tika import parser
import fitz
import PyPDF2 
import streamlit as st

#Local imports
import speech
import dictionary

def read_text():
    input1 = textbox.get("1.0","end-1c")
    speech.text_to_speech(dictionary.Tokenizer(input1))

def read_text_fille():
    root.filename = filedialog.askopenfilename(initialdir='', title="Select file", filetypes=(("txt files","*.txt"),("all files", "*.*")))
    raw = parser.from_file(root.filename)
    speech.text_to_speech(dictionary.Tokenizer(raw['content']))
    
def read_pdf_file():
    pdfdoc = filedialog.askopenfilename(initialdir='', title="Select file", filetypes=(("pdf files","*.pdf"),("all files", "*.*")))
    with fitz.open(pdfdoc) as doc:
        text=""
        for page in doc:
            text +=page.getText() 
    speech.text_to_speech(dictionary.Tokenizer(text))

root = Tk()
root.title('Text to Speech')
root.iconbitmap('logo.ico')
root.geometry("500x500")

textbox = Text(root, width = 50, height = 3, fg = 'red')
textbox.pack()

b1 = Button(root, text = "Text to Speech", padx=5, pady=5, bg='white', fg='green', command=read_text)
b1.pack()

b2 = Button(root, text = "Open Text File", padx=5, pady=5, bg='white', fg='green', command=read_text_fille)
b2.pack()

b3 = Button(root, text = "Open PDF File", padx=5, pady=5, bg='white', fg='green', command=read_pdf_file)
b3.pack()

root.mainloop()

