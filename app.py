import os
import markov
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
   filename='mycorpus.txt'
   markovLength=2
   if (markov.mapping=={}):
	   markov.buildMapping(markov.wordlist(filename),markovLength)
   sentence = markov.genSentence(markovLength)
   return sentence

if __name__ == '__main__':
   #Bind to PORT if defined, otherwise default to 5000.
   port = int(os.environ.get('PORT', 5000))
   app.run(host='0.0.0.0', port=port)
