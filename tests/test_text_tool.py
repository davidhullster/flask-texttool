from flask import Flask
import unittest
import json
from project.text_tool.text_tool import app

class TestTextTool(unittest.TestCase):
    app.testing = True
    client = app.test_client()

    def test_base_route(self):
        response = client.get('/')
        assert response.status_code == 200
