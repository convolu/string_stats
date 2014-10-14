import unittest
import text_stats

class simple_unit_tests(unittest.TestCase):
    '''
    Here go the unit test for the text_stats class
    '''
    def test_empty_string(self):
        '''
        When an empty string is passed, an empty dictionary should
        be returned
        '''
        word_stats = text_stats.text_stats()
        word_stats.extract_stats("")

        self.assertEqual(len(word_stats.freq_table), 0)

    def test_one_word_string(self):
        '''
        Test with input of 1 word
        Please note that all of the input words are turned to lowercase
        '''
        word_stats = text_stats.text_stats()
        word_stats.extract_stats("Hello")

        self.assertEqual(word_stats.freq_table, dict(hello = 1))

    def test_removal_of_dots(self):
        '''
        Test whether dots are removed
        '''
        word_stats = text_stats.text_stats()
        word_stats.extract_stats('Hello. There.')

        self.assertEqual(word_stats.freq_table, dict(hello = 1, there = 1))

    def test_append_to_existing(self):
        '''
        Test whether more results can be appended after processing a string
        '''
        word_stats = text_stats.text_stats()
        word_stats.extract_stats('Hello')

        word_stats.extract_stats('hello')

        self.assertEqual(word_stats.freq_table, dict(hello = 2))

    def test_add_excluded_words(self):
        '''
        Test whether adding a new excluded word works internally
        '''
        word_stats = text_stats.text_stats()
        word_stats.add_excluded_words(['one','two','three'])

        self.assertEqual(word_stats.excluded_words, set(['one','two','three']) )

    def test_append_excluded_words(self):
        '''
        Test whether extending the excluded word set works appropriately
        '''
        word_stats = text_stats.text_stats()
        word_stats.add_excluded_words(['one','two','three'])
        word_stats.add_excluded_words(['four','five','six'])
        self.assertEqual(word_stats.excluded_words,
                         set(['one','two','three','four','five','six']) )

    def test_excluded_word_case(self):
        '''
        Test whether the excluded words are converted into lowercase
        '''
        word_stats = text_stats.text_stats()
        word_stats.add_excluded_words(['One','Two','ThrEe'])

        self.assertEqual(word_stats.excluded_words, set(['one','two','three']) )


    def test_exclusion(self):
        '''
        Test whether excluding a word works
        '''
        word_stats = text_stats.text_stats()
        word_stats.extract_stats('Hello there', ['there'])

        self.assertEqual(word_stats.freq_table, dict(hello=1))


if __name__ == '__main__':
    unittest.main()
