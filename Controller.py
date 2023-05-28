import flask
from flask import request

import configparser

from service.PolarityModel import PolarityModel
from service.PredictionService import PredictionService
from service.SubjectivityModel import SubjectivityModel
from utils.ReviewFactory import ReviewFactory

config = configparser.ConfigParser()
config.read('config.ini')

MODEL_NAME = config['DEFAULT']['model']
BASE_PATH = config['DEFAULT']['base_path']
HOST = config['DEFAULT']['host']
PORT = config['DEFAULT']['port']


def create_app(predict_service):
    app = flask.Flask(__name__)

    @app.route('/polarity', methods=['POST'])
    def infer_polarity():
        data = request.json
        if 'data' not in data.keys():
            return {'message': 'Wrong data formatting'}, 400
        if 'include' not in data.keys():
            return {'message': 'Include labels for polarity not found'}, 400
        predictions = predict_service.predict_polarity(data)
        return predictions, 200

    @app.route('/subjectivity', methods=['POST'])
    def infer_subjectivity():
        data = request.json
        if 'data' not in data.keys():
            return {'message': 'Wrong data formatting'}, 400
        if 'include' not in data.keys():
            return {'message': 'Include labels for subjectivity not found'}, 400
        predictions = predict_service.predict_subjectivity(data)
        return predictions, 200

    @app.route('/combined', methods=['POST'])
    def infer_both():
        data = request.json
        if 'data' not in data.keys():
            return {'message': 'Wrong data formatting'}, 400
        if 'include-polarity' not in data.keys():
            return {'message': 'Include labels for polarity not found'}, 400
        if 'include-subjectivity' not in data.keys():
            return {'message': 'Include labels for subjectivity not found'}, 400
        predictions = predict_service.predict_both(data)
        return predictions, 200

    return app


if __name__ == "__main__":
    # config
    prediction_service = PredictionService(pol_model=PolarityModel(BASE_PATH, MODEL_NAME),
                                           subj_model=SubjectivityModel(BASE_PATH, MODEL_NAME),
                                           review_factory=ReviewFactory())

    # app build
    flask_app = create_app(prediction_service)

    # run
    flask_app.run(host=HOST, port=PORT)
