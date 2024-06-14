from flask import Flask

app = Flask(__name__)

def index():
    return "Hello Miki"

if __name__ == '__main__':
    app.run()