import os

import numpy as np
from transformers import TFAutoModelForSequenceClassification

from models.RobertaModel import RobertaModel


class RobertaPolarityModel(RobertaModel):

    def load(self):
        super().load()
        self.model = TFAutoModelForSequenceClassification.from_pretrained(os.path.join(self.path, 'polarity'))

    def predict(self, data):
        """Make predictions about data"""
        if self.model is None:
            self.load()

        prepared_data = self.prepare_data(data)

        for rev in prepared_data:
            preds = self.model.predict(rev.tensors, verbose=1)['logits']
            rev.predicted_pol = np.argmax(preds, axis=1).tolist()

        self.unload()
