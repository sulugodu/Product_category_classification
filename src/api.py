"""Main script for running the api."""

from flask import Flask,jsonify
from flask_restful import Api, Resource, reqparse
import pickle
from src.model import Model
from src import utils
import os
from pathlib import Path
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

parser = reqparse.RequestParser()
parser.add_argument('input_data')

model_obj = Model()


class ProductCategory(Resource):
    """ """

    def post(self):
        """Function for handling post request."""

        args=parser.parse_args()
        print('got the request')
        test_data = args['input_data']
        status, verified_test_data,id_list = utils.validate_input_data(
            test_data)
        if status:
            try:
                model = model_obj.get_model()
                result = model.predict(verified_test_data)
                result_dict = dict(zip(id_list,result))
                payload = utils.payload(result_dict, status='OK')
            except Exception as ex:
                payload = utils.payload({}, status='Error in the service')
        else:
            payload = utils.payload({}, status='Error in the input data')

        return jsonify(payload)


def load_model():
    """Function for loading the trained model."""
    with open(os.path.join(Path(__file__).resolve().parent,
              '../trained_model/model.pickle'), 'rb') as f:
        model = pickle.load(f)
    model_obj.set_model(model)
    if model_obj.get_model_status():
        print('Product Category Classification model loaded successfully')
        return True
    else:
        return False


def create_app():
    """Creating the Flask app."""
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(ProductCategory, '/products')
    return app


def main():
    """Main script for starting the api."""
    try:
        if load_model():
            app = create_app()
            app.run(debug=True, host='0.0.0.0', port=5000)
        else:
            raise Exception('Model is not loaded')
    except Exception as ex:
        print(ex)
        print("API endpoint is not running. Model is not loaded ")


if __name__ == "__main__":

    main()





