import unittest

from skills1 import *

class TestSkills(unittest.TestCase):

    def setUp(self):
        self.number_list = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
        self.number_list2 = [-4, 2, 16, 8, 22, 5, 101, 2, 22, 7, 50]
        self.word_list = [ "What", "about", "the", "Spam", "sausage", "spam", "spam", "bacon", "spam", "tomato", "and", "spam"]
        self.word_list2 = [ "Hey", "there", "what", "are", "hey", "doing", "whatever", "interesting", "kangaroo", "no"]



    def test_all_odd(self):
        self.assertEqual(all_odd(self.number_list), [-5, 15, 23, 7])
        self.assertEqual(all_odd(self.number_list2), [5, 101, 7])

    def test_all_even(self):
        self.assertEqual(all_even(self.number_list), [6, 4, 8, 16, 42, 2])
        self.assertEqual(all_even(self.number_list2), [-4, 2, 16, 8, 22, 2, 22, 50])

    def test_long_words(self):
        self.assertEqual(long_words(self.word_list), ['What', 'about', 'Spam', 'sausage', 'spam', 'spam', 'bacon', 'spam', 'tomato', 'spam'])
        self.assertEqual(long_words(self.word_list2), ['there', 'what', 'doing', 'whatever', 'interesting', 'kangaroo'])

    def test_smallest(self):
        self.assertEqual(smallest(self.number_list), -5)
        self.assertEqual(smallest(self.number_list2), -4)

    def test_largest(self): 
        self.assertEqual(largest(self.number_list), 42)
        self.assertEqual(largest(self.number_list2), 101)

    def test_halvesies(self):   
        self.assertEqual(halvesies(self.number_list), [-2.5, 3.0, 2.0, 4.0, 7.5, 8.0, 11.5, 21.0, 1.0, 3.5])
        self.assertEqual(halvesies(self.number_list2), [-2.0, 1.0, 8.0, 4.0, 11.0, 2.5, 50.5, 1.0, 11.0, 3.5, 25.0])

    def test_word_lengths(self):
        self.assertEqual(word_lengths(self.word_list), [4, 5, 3, 4, 7, 4, 4, 5, 4, 6, 3, 4])
        self.assertEqual(word_lengths(self.word_list2), [3, 5, 4, 3, 3, 5, 8, 11, 8, 2])      

    def test_sum_numbers(self):
        self.assertEqual(sum_numbers(self.number_list), 118)
        self.assertEqual(sum_numbers(self.number_list2), 231)

    def test_mult_numbers(self):
        self.assertEqual(mult_numbers(self.number_list), -3115929600)
        self.assertEqual(mult_numbers(self.number_list2), -175200256000)

    def test_join_strings(self):
        self.assertEqual(join_strings(self.word_list), 'What about the Spam sausage spam spam bacon spam tomato and spam')
        self.assertEqual(join_strings(self.word_list2), 'Hey there what are hey doing whatever interesting kangaroo no')

    def test_average(self):
        self.assertEqual(average(self.number_list), 11.8)
        self.assertEqual(average(self.number_list2), 21.0)



if __name__ == '__main__':
    unittest.main()
