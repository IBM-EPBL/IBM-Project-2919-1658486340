from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Finance tracker project on Nalaiyadiran initiative, The project is up and running'


if __name__ == '__main__':
    app.run()
