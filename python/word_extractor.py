from search_engine import SearchEngine
from treading import Thread, Lock

class WordExtractor:

	QUERY = "*"
	TARGET_FIELD_NAME = "*"
	RETURN_LIMIT = 10000000
	SPECIAL_CHARACTERS = ["'", "-", ",", ".", "/", "?", ";", ":", "(", ")", "+", "*", "[", "]", "{", "}", "&", "$", "@", "#", "%", "\"", "|", "\\"]
	ENCODING = "utf-8"
	MAX_THREADS = 100

	def __init__(self, collection_url, return_field_name):
		collection_url = collection_url
		target_field_name = WordExtractor.TARGET_FIELD_NAME
		self.return_field_name = return_field_name
		return_limit = WordExtractor.RETURN_LIMIT
		query = WordExtractor.QUERY
		self.url = SearchEngine.build_query_url(collection_url, target_field_name, self.return_field_name, return_limit, query)
		self._word_dict = {}
		self._lock = Lock()

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

	def _add_word_to_dictionary(self, word):
		with self._lock:
			number_of_ocurrences = self._word_dict.get(word, 0) + 1
			self._word_dict[word] = number_of_ocurrences

	def _collect_words(self, data):
		word_list = data.split()
		for word in word_list:
			word = self._treat_word(word)
			if(word is not None):
				self._add_word_to_dictionary

	def extract_words(self):
		response = SearchEngine.query(self.url)
		self._word_dict = {}
		thread_list = []
		for document in response[SearchEngine.DOCUMENTS_KEY]:
			data = document[self.return_field_name]
			thread = Thread(target=self._collect_words, args=(data))
			if(len(thread_list) >= WordExtractor.MAX_THREADS):
				oldest_thread = thread_list[0]
				oldest_thread.join()
				del(thread_list[0])
			thread_list.append(thread)
			thread.start()
		for thread in thread_list:
			thread.join()
		treated_word_list = self._word_dict.keys()
		return treated_word_list