import sys
from word_extractor import WordExtractor
from search_engine import SearchEngine


collection_url = sys.argv[1]
return_field_name = sys.argv[2]
return_limit = 10000000
target_field_name = "*"
query = "*"
search_engine = SearchEngine(collection_url, target_field_name, return_field_name, return_limit)
document_list = search_engine.query(query)
extractor = WordExtractor()
word_list = extractor.extract_words(document_list)
for word in word_list:
	print(word)