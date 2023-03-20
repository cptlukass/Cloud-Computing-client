from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        city_value = request.form['miasto']
        query = requests.get(f'http://127.0.0.1:8000/{city_value}')
        return render_template('final.html', query_result=query.json(), city=city_value.capitalize())


if __name__ == "__main__":
    app.run()
