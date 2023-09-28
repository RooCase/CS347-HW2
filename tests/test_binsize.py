import unittest
import json
import sys
import os
import bin_size
import requests
from flask import Flask

current_dir = os.path.dirname(os.path.abspath(__file__)) # parallel import is weird
parent_dir = os.path.dirname(current_dir) # I know what I am doing, I swear
sys.path.append(parent_dir)

class TestBinPackingAPI(unittest.TestCase):

    def setUp(self):
        bin_size.app.testing = True  # Set the app to testing mode
        self.client = bin_size.app.test_client()  # Create a test clien

    def test_new_problem(self):
        response = self.client.get('/newproblem/100')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('ID' in data)
        self.assertTrue('bins' in data)
        self.assertEqual(data['bins'], "")
        
        # Store the problem ID for later use
        self.problem_id = data['ID']

    def test_place_item(self):
        # Create a new problem
        response = self.client.get('/newproblem/100')
        data = json.loads(response.data)
        problem_id = data['ID']

        # Place an item in the problem
        response = self.client.get(f'/placeItem/{problem_id}/50')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['ID'], problem_id)
        self.assertEqual(data['size'], '50')
        self.assertEqual(data['loc'], 1)  # It should be placed in the first bin

    def test_end_problem(self):
        # Create a new problem
        response = self.client.get('/newproblem/100')
        data = json.loads(response.data)
        problem_id = data['ID']

        # Place some items in the problem
        self.client.get(f'/placeItem/{problem_id}/50')
        self.client.get(f'/placeItem/{problem_id}/40')

        # End the problem
        response = self.client.get(f'/endproblem/{problem_id}')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['ID'], problem_id)
        self.assertEqual(data['size'], 90)  # Total size of items placed
        self.assertEqual(data['items'], 2)  # Number of items placed
        self.assertEqual(data['count'], 1)  # Number of bins used

    def test_invalid_place_item(self):
        # Create a new problem
        response = self.client.get('/newproblem/100')
        data = json.loads(response.data)
        problem_id = data['ID']

        # Attempt to place an item that is too large
        response = self.client.get(f'/placeItem/{problem_id}/150')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('error' in data)
        self.assertEqual(data['error'], 'Problem ID has already been completed or size of item is too large')

if __name__ == '__main__':
    unittest.main()

app = Flask(__name__)
tester = TestBinPackingAPI()
tester.setUp()

@app.route('/')
def hello():
    return "Hello! Welcome to the bin-packing test suite."

@app.route('/test/new')
def test_new():
    tester.test_new_problem()
    return "Test new success!"

@app.route('/test/insert')
def test_place():
    tester.test_place_item()
    return "Test insert success!"

@app.route('/test/invalid_insert')
def test_invalid_place():
    tester.test_invalid_place_item()
    return "Test invalid insert success!"

@app.route('/test/end')
def test_end():
    tester.test_end_problem()
    return "Test end success!"