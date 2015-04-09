"""computing in context social sciences 
data mining utilities
these are fragile and not production code, but here to get you started
to scale them you'll need to start add exceptions
note also that they are not necessarily using the maximally memory
efficient forms of internal representation"""


import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import traceback

def icantbelieve(text):
	print("I can't believe it's not "+text)


def readtextfiles(our_directory):
	"""reads in plain text files and puts them in order in a list"""
	current_dir=os.getcwd()
	os.chdir(our_directory)
	files=[file for file in os.listdir(".") if not file.startswith('.')] #defeat hidden files
	files=[file for file in files if not os.path.isdir(file)==True] #defeat directories

	articles=[]
	for file in files:
	    with open(file, encoding="ascii", errors="surrogateescape") as plaintext:	#ignoring errors insofar as poss
	        lines=plaintext.readlines()
	        article=" ".join(lines) #alter lines if want to skip lines
	        articles.append(article) #you might want to extract the file name to use; how do it?
	os.chdir(current_dir)
	return articles

def data_cleanse(docs_to_clean):
	import re
	D=len(docs_to_clean)
	for d in range(0, D):
	    docs_to_clean[d] = docs_to_clean[d].lower()
	    docs_to_clean[d] = re.sub(r'-', ' ', docs_to_clean[d])
	    docs_to_clean[d] = re.sub(r'[^a-zA-Z0-9 ]', '', docs_to_clean[d])
	    docs_to_clean[d] = re.sub(r' +', ' ', docs_to_clean[d])
	    docs_to_clean[d] = re.sub(r'\s\w\s', ' ', docs_to_clean[d]) #eliminate single letters
	return docs_to_clean

