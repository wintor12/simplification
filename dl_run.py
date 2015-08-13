import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import sent_tokenize
from nltk.corpus import brown
import os
from os.path import join
import numpy as np
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import functions as f


# getTopwords()	

# s = readDoc()
# setting = readSetting()
# model_path = setting[0]
# model = gensim.models.Word2Vec.load_word2vec_format(model_path, binary=True)

# res = ''
# st = LancasterStemmer()
# sent_list = sent_tokenize(s)
# for sentence in sent_list:
# 	text = nltk.word_tokenize(sentence)
# 	tags = nltk.pos_tag(text)

# 	for tag in tags:
# 		word = tag[0]
# 		if checkPos(tag[1]):
# 			if word in model:
# 				word_stem = st.stem(word)  
# 				top_words = model.most_similar(positive=[word], topn = 10)
# 				for w in top_words:
# 					if st.stem(w[0]) != word_stem:  ## exclude morphological derivations 
# 						word = w[0]
# 						break
# 		res = res + word + ' '			
# 	# print model.most_similar(positive=['king'], topn = 20)
# 	# print model.similarity('woman', 'man')

s = f.readDoc()
setting = f.readSetting()
model_path = setting[0]
model = gensim.models.Word2Vec.load_word2vec_format(model_path, binary=True)

news_text = brown.words()
fdist = nltk.FreqDist(w.lower() for w in news_text)

res = ''
st = LancasterStemmer()

text = nltk.word_tokenize(s)
tags = nltk.pos_tag(text)

for tag in tags:
	word = tag[0]
	if f.checkPos(tag[1]):
		if word in model:
			word_stem = st.stem(word)  
			top_words = model.most_similar(positive=[word], topn = 10)
			candidate_list = [w[0] for w in top_words]
			freq_list = [fdist[w] for w in candidate_list]
			c_f_list = zip(candidate_list, freq_list)
			ordered_list = sorted(c_f_list, key=lambda c_f_list:c_f_list[1], reverse=True)
			word_freq = fdist[word]
			synonmys = f.getSynonmys(word)  ## get synonmys from wordnet
			# print synonmys
			for w in ordered_list:
				if not f.freq_diff(word_freq, w[1]):  ## break for loop if candidate word frequency does not exceed the word frequency by a threshold 
					break
				if st.stem(w[0]) != word_stem and f.samePos(word, w[0]): ##exclude morphological derivations and same pos
					if w[0] in synonmys:
						word = w[0]
					else:
						for syn in synonmys:
							if st.stem(w[0]) == st.stem(syn):
								word = w[0]

	res = res + word + ' '	
	
print s
print res