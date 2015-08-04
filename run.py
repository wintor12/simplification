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


# s = 'As MH370 investigators prepare to analyze a Boeing 777 wing component at a French laboratory, ' \
#  'the coastal town where it was found is looking for ways to cement its place in aviation history. ' \
#  'If experts confirm the flaperon is from the missing Malaysia Airlines plane, ' \
#  'it will be the first piece of wreckage found since the jet disappeared 16 months ago. ' \
#  'That would mean the farming town of Saint Andre played a critical role in solving one of the greatest aviation mysteries of modern times. '

s = 'According to Carnell, Behn\'s choice of literary form underscores the differences between her own approach' \
' to crafting a tragic story and that taken in the dramatic tragedies, with their artificial distinction between the public and private spheres. ' \
'Behn\'s novels engage in the political dialogue of her era by demonstrating that the good of the nation ' \
'ultimately encompasses more than the good of the public figures who rule it.'

model_path = '/Users/tongwang/Desktop/exp/lda/GoogleNews-vectors-negative300.bin'
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