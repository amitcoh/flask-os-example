from flask import Flask, render_template
application = Flask(__name__)

TITLE = 'Amit-Test'

@application.route("/")
def hello():
    head = 'Hello!'
    text = 'My name is Amit! I would like to upload this to OpenShift. This is the night deployment test'
    return render_template('index.html', title=TITLE, head=head, text=text)

if __name__ == "__main__":
    application.run()
