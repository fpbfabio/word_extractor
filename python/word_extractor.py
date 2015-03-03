from search_engine import SearchEngine

class WordExtractor:

    QUERY = "*"
    TARGET_FIELD_NAME = "*"
    RETURN_LIMIT = 10000000
    CHARS_TO_IGNORE = [",", ".", "/", "?", ";", ":", "(", ")", "+", "*", "[", "]", "{", "}", "&", "$", "@", "#", "%"]
    HYPHEN = "-"

    def __init__(self, collection_url, return_field_name):
        collection_url = collection_url
        target_field_name = WordExtractor.TARGET_FIELD_NAME
        self.return_field_name = return_field_name
        return_limit = WordExtractor.RETURN_LIMIT
        query = WordExtractor.QUERY
        self.url = SearchEngine.build_query_url(collection_url, target_field_name, self.return_field_name, return_limit, query)

    def extract_words(self):
        response = SearchEngine.query(self.url)
        word_set = set()
        for document in response[SearchEngine.DOCUMENTS_KEY]:
            s = document[self.return_field_name]
            words = s.split()
            num_words = len(words)
            for i in range(0, num_words):
                for c in WordExtractor.CHARS_TO_IGNORE:
                    words[i] = words[i].strip(c)
                words[i] = words[i].lower()
            word_set = word_set.union(set(words))
        return word_set