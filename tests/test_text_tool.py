from flask import Flask
import unittest
import json
from project.text_tool.text_tool import app
app.testing = True
client = app.test_client()

class TestTextTool(unittest.TestCase):

    def test_base_route(self):
        response = client.get('/')
        assert response.status_code == 200
