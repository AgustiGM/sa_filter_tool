import os
import numpy as np

from transformers import TFAutoModelForSequenceClassification, AutoTokenizer

from service.BaseModel import BaseModel
from service.Tokenizer import Tokenizer


class PolarityModel(BaseModel):

    def load(self):
        self.tokenizer = Tokenizer(AutoTokenizer.from_pretrained(self.model_name, return_tensors='tf'))
        self.model = TFAutoModelForSequenceClassification.from_pretrained(os.path.join(self.path, 'custom'))

    def predict(self, data):
        """Make predictions about data"""
        if self.model is None:
            self.load()

        prepared_data = self.prepare_data(data)

        for rev in prepared_data:
            preds = self.model.predict(rev.tensors, verbose=1)['logits']
            rev.predicted_pol = np.argmax(preds, axis=1).tolist()

        self.unload()

    def unload(self):
        self.model = None
        self.tokenizer = None
