"""Contains functions for loading the pickle model."""
from sklearn.pipeline import Pipeline


class Model:
    """A class contain functions for loading the pickle model."""
    def __init__(self, ):
        self.__model = None

    def get_model(self) -> Pipeline:
        """
        Returns ML model.

        :return: trained model
        """
        return self.__model

    def set_model(self, model: Pipeline):
        """
        Loads the ML model into the model instance.

        :param model: model
        """
        self.__model=model

    def get_model_status(self) -> bool:
        """
        Returns status of the model.

        :return: status
        """
        if isinstance(self.__model, Pipeline):
            return True
        else:
            return False

