import unittest

from utils.Review import split_sentences


class TestReview(unittest.TestCase):

    def test_split_sentences_simple(self):
        text = "This is the first sentence. This is the second sentence."
        expected = ["This is the first sentence.", "This is the second sentence."]

        sentences = split_sentences(text)
        self.assertEqual(sentences, expected)

    def test_split_sentences_complex(self):
        text = "I think this app is awesome. Too many annoying ads tho. Stop them!"
        expected = ["I think this app is awesome.", "Too many annoying ads tho.", "Stop them!"]

        sentences = split_sentences(text)
        self.assertEqual(sentences, expected)


if __name__ == '__main__':
    unittest.main()
