from flask import Flask
myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Hello World! I'm Amit"

if __name__ == "__main__":
    myapp.run()
