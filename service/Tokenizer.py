from transformers import AutoTokenizer
from typing import List

from utils.Review import Review


class Tokenizer:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def tokenize(self, reviews: List[Review]):
        for review in reviews:
            review.tensors = list(map(self.tokenizer, review.sentences))

        return reviews
