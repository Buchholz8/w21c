from flask import Flask, request, make_response
import json, jsonify
import dbhelpers

app = Flask(__name__)

app.post("/api/client")
def insert_client():
    error = dbhelpers.check_endpoint_info(request.json, ["username", "password"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedures("call insert_new_client(?,?)", [request.json.get('username', request.json.get('password'))])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"))
    

app.post("/api/login")
def manage_login():
    token = dbhelpers.generate_token
    error = dbhelpers.check_endpoint_info(request.json, ["username", "password"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedures("call insert_new_client(?,?,?)", [request.json.get('username'), request.json.get('password'), token])
    if(type(results) == list):
        return make_response(jsonify({'token': token}), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"))
    

app.post("/api/post")
def new_post():
    error = dbhelpers.check_endpoint_info(request.json, ["token", "content"])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = dbhelpers.run_procedures("call insert_new_client(?,?)", [request.json.get('token', request.json.get('content'))])
                                                                                        
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response(jsonify("Sorry, something went wrong"))