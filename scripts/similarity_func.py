from gensim.corpora import Dictionary
import json
from gensim import corpora
from gensim import similarities
from gensim import models
class VectorEngine():
    def __init__(self):
        self.dictionary = Dictionary.load('~/PycharmProjects/bi-vwm/pageranking/data/page_dictionary.dict')
        
        # print(self.dictionary.token2id['station'])

        corpus = corpora.MmCorpus('~/PycharmProjects/bi-vwm/pageranking/data/corpus.mm')
        self.corpus_lenth = len(corpus)

        self.tfidf = models.TfidfModel(corpus)
        self.corpus_tfidf = self.tfidf[corpus]

    def get_similarity(self, query):
        vec_bow = self.dictionary.doc2bow(query)
        vec_tfidf = self.tfidf[vec_bow]

        index = similarities.MatrixSimilarity(self.corpus_tfidf)
        sims = index[vec_tfidf]
        similarity = list(sims)
        
        # print(similarity)
        end_lenth = len(similarity)
        if self.corpus_lenth != end_lenth:
            print('bug')

        return similarity

vectModel = VectorEngine()

# print( 
#     sorted( list( 
#                 enumerate( 
#                     vectModel.get_similarity(['tunnel'])
#                     )
#                 ),
#             key=lambda tup: tup[1] 
#             )
#     )