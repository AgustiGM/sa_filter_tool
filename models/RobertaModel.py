from transformers import AutoTokenizer

from models.BaseModel import BaseModel
from custom_tokenizers.RobertaTokenizer import RobertaTokenizer


class RobertaModel(BaseModel):

    def load(self):
        self.tokenizer = RobertaTokenizer(AutoTokenizer.from_pretrained(self.model_name, return_tensors='tf'))


