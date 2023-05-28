import unittest
from unittest.mock import MagicMock

from service.Tokenizer import Tokenizer
from utils.Review import Review


class TestTokenizer(unittest.TestCase):
    def setUp(self):
        self.mock_tokenizer = MagicMock()
        self.mock_tokenizer.return_value = ['token1', 'token2', 'token3']
        self.tokenizer = Tokenizer(self.mock_tokenizer)

    def test_tokenize(self):
        # Create mock reviews
        reviews = [
            Review({'id': 1, 'text': 'This is sentence 1.', 'tensors': []}),
            Review({'id': 2, 'text': 'This is sentence 2.', 'tensors': []}),
            Review({'id': 3, 'text': 'Another sentence.', 'tensors': []})
        ]

        tokenized_reviews = self.tokenizer.tokenize(reviews)

        self.assertEqual(len(tokenized_reviews), len(reviews))

        for i in range(len(reviews)):
            review = reviews[i]
            tokenized_review = tokenized_reviews[i]
            self.assertEqual(len(tokenized_review.tensors), len(review.sentences))
            for j in range(len(review.sentences)):
                expected_tokens = ['token1', 'token2', 'token3']
                self.assertEqual(tokenized_review.tensors[j], expected_tokens)


if __name__ == '__main__':
    unittest.main()
