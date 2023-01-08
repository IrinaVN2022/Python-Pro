from flask import Flask
import os
from statistics import mean

app = Flask(__name__)


@app.route('/')
def index():
    with open(os.path.join(app.root_path, 'hw.csv'), encoding='utf-8') as f:
        text = f.read()
    elements = text.split('\n')[1:]
    elements = [element for element in elements if element.strip()]

    heights, weights = [], []
    for element in elements:
        number, height, weight = element.split(",")
        heights.append(float(height))
        weights.append(float(weight))
    avg_height = round(mean(heights)*2.54, 1)
    avg_weight = round(mean(weights) * 2.205, 1)

    return f"average weight: {avg_weight} kg, average height: {avg_height} cm"
app.run(debug=True, port=5000)


