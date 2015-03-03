#!/usr/bin/env python3
from const import UTF8_ENCODING
from urllib.request import urlopen
import json

class SearchEngine:

    JSON_OUTPUT_OPTION = "&wt=json"
    TARGET_FIELD_NAME_AND_QUERY_TERM_SEPARATOR = ":"
    SELECT_FUNCTION_WITH_QUERY_ENTRY = "select?q="
    ROW_OPTION_ENTRY = "&rows="
    FIELD_LIST_OPTION_ENTRY = "&fl="
    RESPONSE_KEY = "response"
    NUMBER_OF_MATCHES_KEY = "numFound"
    DOCUMENTS_KEY = "docs"

    @staticmethod
    def build_query_url(collection_url, target_field_name, return_field_name, return_limit, query):
        select_function = SearchEngine.SELECT_FUNCTION_WITH_QUERY_ENTRY
        separator = SearchEngine.TARGET_FIELD_NAME_AND_QUERY_TERM_SEPARATOR
        json_option = SearchEngine.JSON_OUTPUT_OPTION
        row_option_entry = SearchEngine.ROW_OPTION_ENTRY
        fl_option_entry = SearchEngine.FIELD_LIST_OPTION_ENTRY
        url = collection_url + select_function + target_field_name + separator + query + fl_option_entry + return_field_name + row_option_entry + str(return_limit) + json_option
        return url

    @staticmethod
    def query(url):
        json_response = urlopen(url)
        json_str = json_response.readall().decode(UTF8_ENCODING);
        response = json.loads(json_str)
        return response[SearchEngine.RESPONSE_KEY]
