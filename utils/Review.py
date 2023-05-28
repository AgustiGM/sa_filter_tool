from nltk.tokenize import sent_tokenize


def split_sentences(text):
    return sent_tokenize(text)


class Review:

    def __init__(self, review_dict):
        self.id = review_dict['id']
        self.text = review_dict['text']
        self.sentences = split_sentences(review_dict['text'])
        self.tensors = None
        self.predicted_pol = None
        self.predicted_sub = None


