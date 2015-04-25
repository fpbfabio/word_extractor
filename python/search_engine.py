from urllib.request import urlopen
import json


class SearchEngine:

	ENCODING = "utf-8"
	JSON_OUTPUT_OPTION = "&wt=json"
	TARGET_FIELD_NAME_AND_QUERY_TERM_SEPARATOR = ":"
	SELECT_FUNCTION_WITH_QUERY_ENTRY = "select?q="
	ROW_OPTION_ENTRY = "&rows="
	FIELD_LIST_OPTION_ENTRY = "&fl="
	RESPONSE_KEY = "response"
	NUMBER_OF_MATCHES_KEY = "numFound"
	DOCUMENTS_KEY = "docs"

	def __init__(self, collection_url, target_field_name, return_field_name, return_limit):
		self.collection_url = collection_url
		self.target_field_name = target_field_name
		self.return_field_name = return_field_name
		self.return_limit = return_limit

	def setup(self, collection_url, target_field_name, return_field_name, return_limit):
		self.__init__(collection_url, target_field_name, return_field_name, return_limit)

	def query(self, query):
		select_function = SearchEngine.SELECT_FUNCTION_WITH_QUERY_ENTRY
		separator = SearchEngine.TARGET_FIELD_NAME_AND_QUERY_TERM_SEPARATOR
		json_option = SearchEngine.JSON_OUTPUT_OPTION
		row_option_entry = SearchEngine.ROW_OPTION_ENTRY
		fl_option_entry = SearchEngine.FIELD_LIST_OPTION_ENTRY
		url = self.collection_url + select_function + self.target_field_name + separator + query + fl_option_entry + self.return_field_name + row_option_entry + str(self.return_limit) + json_option
		json_response = urlopen(url)
		json_str = json_response.read().decode(SearchEngine.ENCODING);
		response = json.loads(json_str)
		data_list = []
		for document in response[SearchEngine.RESPONSE_KEY][SearchEngine.DOCUMENTS_KEY]:
			data_list.append(document[self.return_field_name])
		return data_list