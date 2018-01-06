# coding=utf-8

from flask import Flask, jsonify
from flask_pymongo import PyMongo
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'amit_test'
app.config['MONGO_URI'] = 'mongodb://amitc:Password1@172.31.54.173:27017/mydb'

mongo = PyMongo(app)


@app.route('/create_project')
def create_project():
    project = mongo.db.projects
    data = {
        'name': 'Test1',
        'team': 'Sparco',
        'date_added': '5/1/18',
        'due_date': '10/10/18'
    }
    project.insert(data)
    return 'Added!'

@app.route('/')
def home():
    projects = mongo.db.projects
    output = []
    for q in projects.find():
        output.append(q)
    return str(output)



if __name__ == "__main__":
    app.run(debug=True)
