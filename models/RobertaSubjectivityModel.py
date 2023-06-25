import os

import numpy as np
from transformers import TFAutoModelForSequenceClassification

from models.RobertaModel import RobertaModel


class RobertaSubjectivityModel(RobertaModel):

    def load(self):
        super().load()
        self.model = TFAutoModelForSequenceClassification.from_pretrained(os.path.join(self.path, 'subjectivity'))

    def predict(self, data):
        """Make predictions about data"""
        if self.model is None:
            self.load()

        prepared_data = self.prepare_data(data)

        for rev in prepared_data:
            preds = self.model.predict(rev.tensors, verbose=1)['logits']
            rev.subjectivity = np.argmax(preds, axis=1).tolist()

        self.unload()

