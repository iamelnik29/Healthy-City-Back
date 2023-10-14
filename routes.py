from __main__ import app, db
from flask import request
from model import Files
from fictitious_nn import fictitous_function
import json


@app.route("/")
def hello():
    return "It's working!" 

@app.route("/processing", methods=['POST'])
def processing():
    try:
        locality = request.json['locatity']
        res = fictitous_function(locality=locality)
    except:
        try:
            coords_lst = request.json['coords']
            res = fictitous_function(coords=coords_lst)
        except:
            return "Не были направлены данные"
    
    return json.dumps(res)

@app.route("/upload file", methods=['POST'])
def upload_file():
    file = request.files['file']
    new_file = Files(file=file.stream.read())
    db.session.add(new_file)
    db.session.commit()

    return 'OK'
