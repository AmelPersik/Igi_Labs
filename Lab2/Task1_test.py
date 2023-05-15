import unittest
from Task1 import Task1


class TestingClass(unittest.TestCase):

    def setUp(self):

        self.test_text = "Now, Mr. Luis i'll tell u what's math. Math is 3 + 4 =17 (no, 7 but  ok)." \
                         "U don't have to wake up 7 a.m. just to solve ur h0mew0rk. Right, Mrs. teachress? " \
                         "I think so!!!  No integrals & differencials, NO! That's all..." \
                         "It is for ngrams.. It is for ngrams beibah!"
        self.test_n = 2
        self.test_k = 5
        self.result = Task1(self.test_text, self.test_n, self.test_k)

        self.expected_num_of_ss = 9
        self.expected_num_of_ndss = 4
        self.expected_aver_length_of_ss = 18.11111
        self.expected_aver_length_of_w = 3.46808
        self.expected_top_nk = [('It is', 2), ('is for', 2), ('for ngrams', 2), ('Now Mr.', 1), ('Mr. Luis', 1)]




    def test_sentences_number(self):
        self.assertEqual(self.result[0], self.expected_num_of_ss)

    def test_nondeclarative_sentences_number(self):
        self.assertEqual(self.result[1], self.expected_num_of_ndss)

    def test_average_sentence_length(self):
        self.assertAlmostEqual(self.result[2], self.expected_aver_length_of_ss, delta = 0.0001)

    def test_average_word_lenght(self):
        self.assertAlmostEqual(self.result[3], self.expected_aver_length_of_w, delta = 0.0001)

    def test_expected_topk_of_ngrams(self):
        self.assertEqual(self.result[4], self.expected_top_nk)