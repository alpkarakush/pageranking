from pprint import pprint  # pretty-printer
from collections import defaultdict
from gensim.parsing.preprocessing import preprocess_string
from gensim.corpora import Dictionary
import json
from gensim import corpora
from tqdm import tqdm
dictionary = Dictionary.load( "../data/page_dictionary.dict" )

with open('../data/spider.json', mode='r') as json_pages:
    data = json.load(json_pages)

# # tokenids,token of words, that appear only once
# once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.items() if docfreq == 1]
# once_tokens = [token for token, freq in dictionary.token2id.items() if freq == 1]

# #remove words, that appear only once from dictionary
# dictionary.filter_tokens(once_ids)
# dictionary.compactify()

corpus = []

#delete stopwords, lowercase, strip numeric, strip punctuation  and convert to vec form
for page in tqdm(data):
	page['text'] = preprocess_string( page['text'] )
	# page['text'] = [ token for token in page['text'] if token not in once_tokens ]
	corpus.append( dictionary.doc2bow( page['text'] ) )		# [ [ tokenid ] , [ freq ] ]


corpora.MmCorpus.serialize('../data/corpus.mm', corpus)