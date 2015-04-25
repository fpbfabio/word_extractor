from search_engine import SearchEngine


class WordExtractor:

	QUERY = "*"
	TARGET_FIELD_NAME = "*"
	RETURN_LIMIT = 10000000
	SPECIAL_CHARACTERS = ["'", "-", ",", ".", "/", "?", ";", ":", "(", ")", "+", "*", "[", "]", "{", "}", "&", "$", "@", "#", "%", "\"", "|", "\\"]
	ENCODING = "utf-8"

	def __init__(self, collection_url, return_field_name):
		collection_url = collection_url
		target_field_name = WordExtractor.TARGET_FIELD_NAME
		self.return_field_name = return_field_name
		return_limit = WordExtractor.RETURN_LIMIT
		query = WordExtractor.QUERY
		self.url = SearchEngine.build_query_url(collection_url, target_field_name, self.return_field_name, return_limit, query)

	def _treat_word(self, word)
		word = str(word.encode(WordExtractor.ENCODING))[1:].strip("'")
		word = word.replace("\\", "")
		for character in WordExtractor.SPECIAL_CHARACTERS:
			word = word.strip(character)
			if(character in word):
				return None
		if(len(word) <= 1)
			return None
		word = word.lower()
		return word

	def extract_words(self):
		response = SearchEngine.query(self.url)
		word_dict = {}
		for document in response[SearchEngine.DOCUMENTS_KEY]:
			data = document[self.return_field_name]
			word_list = data.split()
			for word in word_list:
				word = self._treat_word(word)
				if(word is not None):
					number_of_ocurrences = word_dict.get(word, 0) + 1
					word_dict[word] = number_of_ocurrences
		treated_word_list = word_dict.keys()
		return treated_word_list