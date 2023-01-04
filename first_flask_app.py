from flask import Flask
import os
from util import format_list

app = Flask(__name__)


@app.route('/')
def index():
    with open(os.path.join(app.root_path, 'requirements.txt'), encoding='utf-16') as f:
        text = f.read()
    elements = text.split('\n')
    elements = [element for element in elements if element.upper().isupper()]

    return format_list(elements)


app.run(debug=True)
