from threading import Thread, Lock


class WordExtractor:

	INVALID_CHARACTERS = ["'", ",", ".", "/", "?", ";", ":", "(", ")", "+", "*", "[", "]", "{", "}", "&", "$", "@", "#", "%", "\"", "|", "\\", ">", "<", "!", "=", "(", ")", "`"]
	NUMBERS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
	HIFEN = "-"
	ENCODING = "utf-8"
	MAX_THREADS = 100

	def __init__(self):
		self._word_dict = {}
		self._lock = Lock()

	def _treat_word(self, word):
		word = str(word.encode(WordExtractor.ENCODING)).lstrip("b").strip("'")
		word = word.replace("\\", "")
		for character in WordExtractor.INVALID_CHARACTERS:
			word = word.strip(character).strip(character)
			if(character in word):
				return None
		for character in WordExtractor.NUMBERS:
			if(character in word):
				return None
		word = word.strip(WordExtractor.HIFEN).strip(WordExtractor.HIFEN)
		if(len(word) <= 3):
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
				self._add_word_to_dictionary(word)

	def extract_words(self, data_list):
		self._word_dict = {}
		thread_list = []
		for data in data_list:
			thread = Thread(target=self._collect_words, args=([data]))
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