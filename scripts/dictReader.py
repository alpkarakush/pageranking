from gensim.corpora import Dictionary
import json
from lxml.html.clean import Cleaner
from gensim.parsing.preprocessing import preprocess_string
from tqdm import tqdm

dictionary = Dictionary()

with open('../data/spider.json', mode='r') as json_pages:
    data = json.load(json_pages)

cleaner = Cleaner()
cleaner.javascript = True # This is True because we want to activate the javascript filter
cleaner.style = True      # This is True because we want to activate the styles & stylesheet filter

for page in tqdm(data):
	dictionary.add_documents( [ preprocess_string(page['text'] ) ,] )

dictionary.save("~/PycharmProjects/bi-vwm/pageranking/data/page_dictionary.dict")
