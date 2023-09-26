import requests
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    message = "Welcome! Use /Alex to benchmark the original API. Use /Carla to benchmark the modified API."  
    return {message}

@app.route('/Alex')
def alex():
    return {"Alex"}

@app.route('/Carla')
def carla():
    return {"Carla"}

if __name__ == '__main__':
    app.run(port=5000)