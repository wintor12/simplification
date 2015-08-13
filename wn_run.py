import nltk
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import sent_tokenize
from nltk.corpus import brown
import os
from os.path import join
import functions as f
from nltk.corpus import wordnet

res = []
syns = wordnet.synsets('forceful')
for s in syns:
	for l in s.lemmas:
		res.append(l.name)

res = list(set(res))
print res


# s = f.readDoc()
# setting = f.readSetting()

# news_text = brown.words()
# fdist = nltk.FreqDist(w.lower() for w in news_text)

# res = ''
# st = LancasterStemmer()

# text = nltk.word_tokenize(s)
# tags = nltk.pos_tag(text)

# for tag in tags:
# 	word = tag[0]
# 	if f.checkPos(tag[1]):
# 		# if word in model:
# 		# 	word_stem = st.stem(word)  
# 		# 	top_words = model.most_similar(positive=[word], topn = 10)
# 		# 	max_freq = fdist[word]
# 		# 	max_freq_word = word
# 		# 	for w in top_words:
# 		# 		if st.stem(w[0]) != word_stem and f.samePos(word, w[0]): ##exclude morphological derivations and same pos
# 		# 			candidate = w[0]
# 		# 			if fdist[candidate] > max_freq:
# 		# 				max_freq = fdist[candidate]
# 		# 				max_freq_word = candidate
# 		# 	word = max_freq_word
# 		pass
# 	res = res + word + ' '	
	
# print s
# print res