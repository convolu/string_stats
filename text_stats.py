class text_stats():
    def __init__(self):
        '''
        Class initialisation, this class initialises the list of words that is
        used internally and the frequency table print_sorted_dictionary
        '''
        self.word_list = []
        self.freq_table = {}
        self.excluded_words = set()
        self.total_words = 0

    def __list_from_text(self, text):
        '''
        This function takes a string as an input and returns a list of the
        words. This function assumes that the words are whitespace delimited.
        Each of the words is not unique.
        '''

        #.split() removes empty strings
        ret_list = text.split() if len(text) > 0 else []
        self.word_list = ret_list

    def __clean_trailing_symbols(self, text):
        '''
        This function takes a string as an input and it returns the string
        removing the trailing symbols if they exist, otherwise it returns the
        string as is. If the string given as a parameter is empty an
        empty string is returned
        '''
        symbols = ['.', '!', ',', ')']
        ret = ''

        if (len(text) > 0) and (text[-1] in symbols):
            ret = text[:len(text) - 1]
        else:
            ret = text
        return ret

    def __remove_empty_strings(self, words):
        '''
        This function uses list comprehension to remove empty elements from
        the list
        '''
        return [word for word in words if len(word) > 0]

    def __remove_case_from_list(self, words):
        '''
        This function takes the list of words and forces lowercase so as to
        prepare for the frequency count
        '''
        return [word.casefold() for word in words]

    def __tidy_list(self):
        '''
        This function removes trailing symbols and empty entries from the list
        as well as forces lowercase to prepare for the word frequency count
        '''

        self.word_list[:] = self.__remove_empty_strings(self.word_list)

        self.word_list[:] = map(self.__clean_trailing_symbols, self.word_list)

        self.word_list[:] = self.__remove_case_from_list(self.word_list)

    def __count_word_frequency(self, words):
        '''
        This function updates the dictionary with the count of
        '''
        freq_table = self.freq_table

        for word in words:
            if word not in freq_table.keys():
                freq_table[word] = 1
            else:
                freq_table[word] += 1
        return freq_table

    def add_excluded_words(self, ecl_words):
        lowercase_ecl_words = self.__remove_case_from_list(ecl_words)
        self.excluded_words.update(set(lowercase_ecl_words))

    def remove_excluded_words(self):

        for word in self.excluded_words:
            if word in self.freq_table:
                del self.freq_table[word]

    def print_sorted_dictionary(self, dict_table):
        for freq, word in sorted(dict_table.items(),
                                 key=lambda x: (-1*x[1], x[0])):
            print("Count:{0:3d} - \'{1:s}\'".format(word, freq))

    def extract_stats(self, text, excl=[]):
        self.__list_from_text(text)
        self.__tidy_list()
        self.__count_word_frequency(self.word_list)
        self.add_excluded_words(excl)
        self.remove_excluded_words()
        self.word_list.clear()
        self.__update_total_words()

    def __calculate_total_words(self):
        return sum(self.freq_table.values())

    def __update_total_words(self):
        self.total_words = self.__calculate_total_words()

    def get_total_words(self):
        self.__update_total_words()
        return self.total_words
