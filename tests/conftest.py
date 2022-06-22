"""Functions for setup test configurations."""

import pytest

from src.api import create_app, load_model


@pytest.fixture()
def app():
    load_model()
    app=create_app()
    app.config.update({"TESTING":True,})
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()