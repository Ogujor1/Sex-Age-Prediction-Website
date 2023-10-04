from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return 'Add to the link; /guess/your name'


@app.route('/guess/<name>')
def your_name(name):
    param = {'name': name}
    age_api = 'https://api.agify.io'
    gen_api = 'https://api.genderize.io'
    request_age = requests.get(age_api, params=param)
    request_gen = requests.get(gen_api, params=param)
    data_age = request_age.json()['age']
    data_name = request_age.json()['name']
    data_gen = request_gen.json()['gender']
    return render_template('index.html', name=data_name, age=data_age, gender=data_gen)


if __name__ == "__main__":
    app.run(debug=True)
