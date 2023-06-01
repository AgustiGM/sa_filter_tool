from collections import defaultdict
from typing import List

from datasets import Dataset
from transformers import DataCollatorWithPadding
import tensorflow as tf
from utils.Review import Review


class Tokenizer:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer, return_tensors='tf')

    def aux_tokenize(self, example):
        return self.tokenizer(example['text'], truncation=True)

    def tokenize(self, reviews: List[Review]):
        for review in reviews:
            ds = {'text': []}
            for sent in review.sentences:
                ds['text'].append(sent)
            ds = Dataset.from_dict(ds)
            review.tensors = ds.map(self.aux_tokenize, batched=True)
            review.tensors.set_format(type='tf',
                                      columns=['attention_mask', 'input_ids'])
            review.tensors = review.tensors.to_tf_dataset(
                columns=['input_ids', 'attention_mask'],
                shuffle=False,
                collate_fn=self.data_collator,
                batch_size=8
            )

        return reviews
