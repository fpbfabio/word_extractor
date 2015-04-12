#!/usr/bin/env python3

import sys
from word_extractor import WordExtractor

extractor = WordExtractor(sys.argv[1], sys.argv[2])
word_list = extractor.extract_words()
for word in word_list:
	print(word)