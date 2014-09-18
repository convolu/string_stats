class word_distribution():
    def __init__(self):
        '''
        Class initialisation, this class initialises the list of words that is
        used internally and the frequency table print_sorted_dictionary
        '''
        self.word_list = []
        self.freq_table = {}

    def __list_from_text(self, text):
        '''
        This function takes a string as an input and returns a list of the words.
        This function assumes that the words are whitespace delimited.
        Each of the words is not unique.
        '''
        ret_list = []

        if len(text) > 0:
            ret_list = text.split() #.split() removes empty strings

        self.word_list = ret_list

    def __clean_trailing_symbols(self, text):
        '''
        This function takes a string as an input and it returns the string removing
        the trailing symbols if they exist, otherwise it returns the string as is
        If the string given as a parameter is empty an empty string is returned
        '''
        symbols =['.', '!', ',', ')']
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
        words[:] = [word for word in words if len(word) > 0]

    def __remove_case(self, text):
        return text.casefold()

    def __remove_case_from_list(self, words):
        '''
        This function takes the list of words and forces lowercase so as to
        prepare for the frequency count
        '''
        for i in range(len(words)):
            words[i] = self.__remove_case(words[i])

    def __tidy_list(self):
        '''
        This function removes trailing symbols and empty entries from the list
        as well as forces lowercase to prepare for the word frequency count
        '''
        for i in range(len(self.word_list)):
            self.word_list[i] = self.__clean_trailing_symbols(self.word_list[i])

        self.__remove_empty_strings(self.word_list)
        self.__remove_case_from_list(self.word_list)

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

    def print_sorted_dictionary(self, dict_table):
        for item in sorted(dict_table.items(),
                           key = lambda x: (x[1], x[0]),
                           reverse = True
                           ):
            print("Count: %i - \'%s\'" % (item[1], item[0]))

    def extract_stats(self, text):
        self.__list_from_text(text)
        self.__tidy_list()
        self.__count_word_frequency(self.word_list)
        self.word_list.clear()

#Text from 'http://en.wikipedia.org/wiki/Electric_charge'
wiki_text = """ Electric charge is the physical property of matter that causes
                it to experience a force when placed in an electromagnetic
                field. There are two types of electric charges: positive and
                negative. Positively charged substances are repelled from
                other positively charged substances, but attracted to
                negatively charged substances; negatively charged substances
                are repelled from negative and attracted to positive. An
                object is negatively charged if it has an excess of electrons,
                and is otherwise positively charged or uncharged. The SI
                derived unit of electric charge is the coulomb (C), although
                in electrical engineering it is also common to use the
                ampere-hour (Ah), and in chemistry it is common to use the
                elementary charge (e) as a unit. The symbol Q is often used to
                denote charge. The early knowledge of how charged substances
                interact is now called classical electrodynamics, and is still
                very accurate if quantum effects do not need to be considered.
                The electric charge is a fundamental conserved property of
                some subatomic particles, which determines their
                electromagnetic interaction. Electrically charged matter is
                influenced by, and produces, electromagnetic fields. The
                interaction between a moving charge and an electromagnetic
                field is the source of the electromagnetic force, which is one
                of the four fundamental forces (See also: magnetic field).
                Twentieth-century experiments demonstrated that electric
                charge is quantized; that is, it comes in integer multiples
                of individual small units called the elementary charge, e,
                approximately equal to 1.602×10−19 coulombs (except for
                particles called quarks, which have charges that are integer
                multiples of e/3). The proton has a charge of +e, and the
                electron has a charge of −e. The study of charged particles,
                and how their interactions are mediated by photons, is called
                quantum electrodynamics.
            """

#TODO add option for input parameters, maybe use file or url
def main():
    word_stats = word_distribution()
    word_stats.extract_stats(wiki_text)
    word_stats.print_sorted_dictionary(word_stats.freq_table)


if __name__ == '__main__':
    main()
