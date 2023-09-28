import requests
from flask import Flask
from flask import render_template
import evaluate

app = Flask(__name__)

@app.route('/')
def main():
    message = "Welcome! Use /Alex to benchmark the original API. Use /Carla to benchmark the modified API."  
    return message

@app.route('/Alex')
def alex_place():
    evaluator = evaluate.Evaluation("Alex")
    time = evaluator.main()
    return str(time)

@app.route('/Carla')
def carla_place():
    evaluator = evaluate.Evaluation("Carla")
    time = evaluator.main()
    return str(time)

if __name__ == '__main__':
    app.run(port=5000)