# import tensorflow as tf

from transformers import AutoTokenizer

from service.Tokenizer import Tokenizer


class BaseModel:
    def __init__(self, path, model_name):
        self.path = path
        self.model_name = model_name
        self.tokenizer = Tokenizer(model_name)

    def load(self):
        """Load in model for inferencing."""
        pass

    def predict(self, data):
        """Make predictions about data"""
        pass
