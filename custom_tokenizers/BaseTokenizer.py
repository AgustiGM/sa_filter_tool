from typing import List

from utils.Review import Review


class BaseTokenizer:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def tokenize(self, reviews: List[Review]):
        """Function to prepare data for inferencing"""
        raise NotImplementedError
