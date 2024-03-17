from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p><b>Hello, World!</b></p>"

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

if __name__ == "__main__":
    app.run()