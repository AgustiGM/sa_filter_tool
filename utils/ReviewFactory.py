from utils.Review import Review


class ReviewFactory:
    @staticmethod
    def create_review(review_dict):
        return Review(review_dict)

    @staticmethod
    def common_mapper(review: Review, attribute, values):
        result = {
            'id': review.id,
            'text': []
        }

        for sentence, val in zip(review.sentences, getattr(review, attribute)):
            if val in values:
                result['text'].append(sentence)

        return result

    @staticmethod
    def both_common_mapper(review: Review, values_pol, values_subj):
        result = {
            'id': review.id,
            'text': []
        }

        for sentence, pol, subj in zip(review.sentences, review.predicted_pol, review.predicted_sub):
            if pol in values_pol and subj in values_subj:
                result['text'].append(sentence)

        return result

    @staticmethod
    def return_polarity_ok(values: list):
        def pol_mapper(review: Review):
            return ReviewFactory.common_mapper(review, "predicted_pol", values)

        return pol_mapper

    @staticmethod
    def return_subjectivity_ok(values: list):
        def sub_mapper(review: Review):
            return ReviewFactory.common_mapper(review, "predicted_sub", values)

        return sub_mapper

    @staticmethod
    def return_both_ok(values_pol: list, values_subj: list):
        def both_mapper(review: Review):
            return ReviewFactory.both_common_mapper(review,values_pol, values_subj)

        return both_mapper
