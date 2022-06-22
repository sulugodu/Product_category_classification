"""Util function for RESTAPI."""
import pandas as pd
import json


def payload(prediction: dict, status: str)-> dict:
    """

    Packs the result  and status src into payload.

    :param prediction: prediction result
    :param status: result status
    :return: payload
    """
    return {'status': status, 'prediction': prediction}


def validate_input_data(input_data:json):
    """

    Validates the input data.

    :param input_data: json data
    """
    data_frame = pd.read_json(input_data, orient='index')
    if 'main_text' in data_frame.columns and 'add_text' in data_frame.columns:
        data_frame['description'] = data_frame['main_text'].astype(str) + ' ' + data_frame['add_text'].astype(str)
        data_frame = data_frame.dropna(subset= ['description', 'id'])
        if not data_frame.empty:
            return True, data_frame['description'], data_frame['id'].tolist()

    return False, None,None

