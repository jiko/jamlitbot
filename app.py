import os
import string
import markov
from bottle import route, run

@route('/')
@route('/<r>')
def hello(r="hf9831h1rgfewuifgasjkbzxg1e"):
   filename='mycorpus.txt'
   markovLength=3
   if (markov.mapping=={}):
	   markov.buildMapping(markov.wordlist(filename),markovLength)
   sentence = markov.genSentence(markovLength, r.lower())
   page = "<!DOCTYPE html><html><header><title>JAMLITBOT</title><style type='text/css'>a {color:black;text-decoration:none}</style></header><body>"
   for word in sentence.split():
		page += "<a href='"+word.translate(string.maketrans("",""),string.punctuation)+"'>"+word+"</a> "
   page += "<br><br><a href='/'>reload</a></body></html>"
   return page

run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
