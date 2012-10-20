import os
import markov
from bottle import route, run
app = Flask(__name__)

@route('/')
@route('<r>')
def hello(r):
   filename='mycorpus.txt'
   markovLength=2
   if (markov.mapping=={}):
	   markov.buildMapping(markov.wordlist(filename),markovLength)
   sentence = markov.genSentence(markovLength)
   return sentence

run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
