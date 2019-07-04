from .similarity_func import VectorEngine
from gensim.parsing.preprocessing import preprocess_string
import json
import numpy as np

class SearchEngine():
    def __init__(self):
        self.vectEngine = VectorEngine()

        with open('./data/page_ranking.json', mode='r') as ranks:
            self.pagerank = json.load(ranks)

    def query(self, searchText):
        searchText = preprocess_string(searchText)

        vectResult = self.vectEngine.get_similarity( searchText )

        #multiply pageranks and vectResult
        result = np.multiply( np.array(vectResult), np.array(self.pagerank))

        #get best 10 results
        result = sorted( list( enumerate( result ) ), key=lambda tup: tup[1] , reverse=True )
        result = result[:10]

        with open('./data/spider.json', mode='r') as data:
            pages = json.load(data)
            links = [ page['link'] for page in pages]

        result = [ links[ int(key) ]  for key, val in result ]

        return result

# engine = SearchEngine()
# engine.query("The tunnel")
        