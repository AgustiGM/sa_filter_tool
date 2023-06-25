import unittest
from unittest.mock import MagicMock
from utils.Review import Review
from service.PredictionService import PredictionService


class TestPredictionService(unittest.TestCase):
    def setUp(self):
        self.mock_model = MagicMock()
        self.mock_review_factory = MagicMock()
        self.service = PredictionService(self.mock_model, self.mock_model, self.mock_review_factory)

        self.review_data = {
            'data': [
                {'id': 1, 'text': 'This is a positive review.'},
                {'id': 2, 'text': 'This is a negative review.'}
            ],
            'include': [1, 2]
        }

    def test_predict_polarity(self):
        review1 = Review({'id': 1, 'text': 'This is a positive review.'})
        review2 = Review({'id': 2, 'text': 'This is a negative review.'})
        self.mock_review_factory.create_review.side_effect = [review1, review2]

        expected_results = [
            {'id': 1, 'text': ['This is a positive review.']},
            {'id': 2, 'text': ['This is a negative review.']}
        ]

        mapper_mock = MagicMock()
        mapper_mock.side_effect = [
            {'id': 1, 'text': ['This is a positive review.']},
            {'id': 2, 'text': ['This is a negative review.']}
        ]
        self.mock_review_factory.return_polarity_ok.return_value = mapper_mock

        results = self.service.predict_polarity(self.review_data)

        self.assertEqual(results, expected_results)
        self.mock_model.predict.assert_called_once_with([review1, review2])
        self.mock_review_factory.return_polarity_ok.assert_called_once_with(self.review_data['include'])
        mapper_mock.assert_called()

    def test_predict_subjectivity(self):
        review1 = Review({'id': 1, 'text': 'This is a subjective review.'})
        review2 = Review({'id': 2, 'text': 'This is an objective review.'})
        self.mock_review_factory.create_review.side_effect = [review1, review2]

        expected_results = [
            {'id': 1, 'text': ['This is a subjective review.']},
            {'id': 2, 'text': ['This is an objective review.']}
        ]

        mapper_mock = MagicMock()
        mapper_mock.side_effect = [
            {'id': 1, 'text': ['This is a subjective review.']},
            {'id': 2, 'text': ['This is an objective review.']}
        ]
        self.mock_review_factory.return_subjectivity_ok.return_value = mapper_mock

        results = self.service.predict_subjectivity(self.review_data)

        self.assertEqual(results, expected_results)
        self.mock_model.predict.assert_called_once_with([review1, review2])
        self.mock_review_factory.return_subjectivity_ok.assert_called_once_with(self.review_data['include'])
        mapper_mock.assert_called()


    def tearDown(self):
        self.mock_model.reset_mock()
        self.mock_review_factory.reset_mock()


if __name__ == '__main__':
    unittest.main()
