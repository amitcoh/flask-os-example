from flask import Flask, render_template

TITLE = 'Amit-Test'

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html', title=TITLE)


if __name__ == "__main__":
    app.run()