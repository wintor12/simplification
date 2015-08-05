import nltk
from nltk.stem.lancaster import LancasterStemmer
import os
from os.path import join
import numpy as np
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def checkPos(word):
	pos = ['NN', 'NNS', 'JJ', 'RB', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
	if word in pos:
		return True
	else:
		return False

def readSetting():
	path = os.getcwd()
	with open(join(path, 'setting'), 'r') as f:
		setting = f.readlines()
	return setting

def readDoc():
	path = os.getcwd()
	p = open(join(path, 'doc'), 'r')
	s = p.read()
	p.close()
	return s

s = readDoc()
setting = readSetting()
model_path = setting[0]
model = gensim.models.Word2Vec.load_word2vec_format(model_path, binary=True)

res = ''
text = nltk.word_tokenize(s)
tags = nltk.pos_tag(text)
st = LancasterStemmer()
for tag in tags:
	word = tag[0]
	if checkPos(tag[1]):
		if word in model:
			word_stem = st.stem(word)  
			top_words = model.most_similar(positive=[word], topn = 10)
			for w in top_words:
				if st.stem(w[0]) != word_stem:  ## exclude morphological derivations 
					word = w[0]
					break
	res = res + word + ' '			
# print model.most_similar(positive=['king'], topn = 20)
# print model.similarity('woman', 'man')

print s
print res