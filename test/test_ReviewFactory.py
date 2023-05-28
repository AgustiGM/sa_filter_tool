import unittest
from utils.Review import Review
from utils.ReviewFactory import ReviewFactory


class TestReviewFactory(unittest.TestCase):

    def setUp(self):
        review1 = Review({'id': 1, 'text': 'This is a positive review. This is a negative sentence'})
        review1.sentences = ['This is a positive review.', 'This is a negative sentence']
        review1.predicted_pol = [3, 1]
        review1.predicted_sub = [0, 1]

        review2 = Review({'id': 2, 'text': 'This is a neutral review. However, this is a positive aspect.'})
        review2.sentences = ['This is a neutral review.', 'However, this is a positive aspect.']
        review2.predicted_pol = [2, 3]
        review2.predicted_sub = [2, 1]

        review3 = Review(
            {'id': 3, 'text': 'This is a negative review. Very very negative. You cannot fathom the negativity.'})
        review3.sentences = ['This is a negative review.', 'Very very negative.', 'You cannot fathom the negativity.']
        review3.predicted_pol = [1, 0, 0]
        review3.predicted_sub = [1, 2, 2]

        self.review_list = [review1, review2, review3]

    def test_create_review(self):
        review_dict = {'id': 1, 'text': 'This is a review.'}
        review = ReviewFactory.create_review(review_dict)
        self.assertEqual(review.id, 1)
        self.assertEqual(review.text, 'This is a review.')

    def test_return_polarity_ok(self):
        values = [3, 4]
        mapper = ReviewFactory.return_polarity_ok(values)
        result = list(map(mapper, self.review_list))
        expected = [
            {'id': 1, 'text': ['This is a positive review.']},
            {'id': 2, 'text': ['However, this is a positive aspect.']},
            {'id': 3, 'text': []}
        ]
        self.assertEqual(result, expected)

    def test_return_subjectivity_ok(self):
        values = [0, 2]
        mapper = ReviewFactory.return_subjectivity_ok(values)
        result = list(map(mapper, self.review_list))
        expected = [
            {'id': 1, 'text': ['This is a positive review.']},
            {'id': 2, 'text': ['This is a neutral review.']},
            {'id': 3, 'text': ['Very very negative.', 'You cannot fathom the negativity.']}
        ]
        self.assertEqual(result, expected)

    def test_return_both_ok(self):
        values_pol = [3, 2]
        values_subj = [0]
        mapper = ReviewFactory.return_both_ok(values_pol, values_subj)
        result = list(map(mapper, self.review_list))
        expected = [
            {'id': 1, 'text': ['This is a positive review.']},
            {'id': 2, 'text': []},
            {'id': 3, 'text': []}
        ]
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
