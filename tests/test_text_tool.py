from flask import Flask
import json
from project.text_tool import app

app.testing = True
client = app.test_client()

def test_base_route():
    response = client.get('/')
    assert response.status_code == 200
