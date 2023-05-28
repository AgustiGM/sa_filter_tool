from service.PolarityModel import PolarityModel
from utils.Review import Review


class PredictionService:

    def __init__(self, pol_model, subj_model, review_factory):
        self.polarity_model = pol_model
        self.subjectivity_model = subj_model
        self.review_factory = review_factory

    def predict_polarity(self, data):
        reviews = []
        for item in data['data']:
            reviews.append(self.review_factory.create_review(item))

        self.polarity_model.predict(reviews)
        mapper = self.review_factory.return_polarity_ok(data['include'])
        results = list(map(mapper, reviews))

        return results

    def predict_subjectivity(self, data):
        reviews = []
        for item in data['data']:
            reviews.append(self.review_factory.create_review(item))

        self.subjectivity_model.predict(reviews)
        mapper = self.review_factory.return_subjectivity_ok(data['include'])
        results = list(map(mapper, reviews))

        return results

    def predict_both(self, data):
        reviews = []
        for item in data['data']:
            reviews.append(self.review_factory.create_review(item))

        self.polarity_model.predict(reviews)
        self.subjectivity_model.predict(reviews)

        mapper = self.review_factory.return_both_ok(values_pol=data['include-polarity'],
                                                    values_subj=data['include-subjectivity'])

        results = list(map(mapper, reviews))
        return results
