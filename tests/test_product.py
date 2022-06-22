"""Unit test case for api end point"""

import pandas as pd
import json

test_data = pd.DataFrame({'id': [25646138],	'main_text': ["HOLLANDRAD DAMEN "
                                                            "28 ZOLL TUSSAUD 3-GAENGE RH 54 cm  SCHWARZ BELLEFLEUR"],
"add_text":	["FAHRRAEDER // SPORTFAHRRAEDER"],"manufacturer":["SCHALOW & KROH GMBH"]})


def test_api(client):
    """Ideal result"""
    response = client.post("/products", json={'input_data': test_data.to_json(orient='index')})
    assert response.status_code == 200
    assert json.loads(response.text)['status'] == 'OK'


test_data_error = pd.DataFrame({'id': [25646138],	'main_text': [None],
                        "manufacturer":[None]})


def test_api_error(client):
    response = client.post("/products", json={'input_data': test_data_error.to_json(orient='index')})
    print(response)
    assert response.status_code == 200
    assert json.loads(response.text)['status'] == 'Error in the input data'
