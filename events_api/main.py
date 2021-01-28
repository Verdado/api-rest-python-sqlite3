from flask import Flask, jsonify, request, make_response, json
import event_controller
from db import create_event, create_user, signed_events
from helper.email_invite import email_invite

app = Flask(__name__)

@app.route('/events', methods=["GET"])
def get_events():
    events = event_controller.get_events()
    dict = {}
    dict["events"] = events
    return jsonify(events)
    #return jsonify(dict)

@app.route('/users', methods=["GET"])
def get_users():
    users = event_controller.get_users()
    dict = {}
    dict["users"] = users
    return dict

@app.route("/events/<event_uid>", methods=["GET"])
def get_event_info(event_uid):
    events = event_controller.get_event_info(event_uid)
    dict = {}
    dict["event_info"] = events
    return jsonify(events)

@app.route("/event_users/<event_uid>", methods=["GET"])
def event_users(event_uid):
    result = event_controller.get_event_users(event_uid)
    dict = {}
    dict["signed_users"] = result
    return dict

@app.route("/event", methods=["POST"])
def insert_event():
    event_details = request.get_json()
    name = event_details["name"]
    location = event_details["location"]
    start_timestamp = event_details["start_timestamp"]
    end_timestamp = event_details["end_timestamp"]
    result = event_controller.insert_event(name, location, start_timestamp, end_timestamp)
    return make_response(jsonify(result), 201)

@app.route("/user", methods=["POST"])
def insert_user():
    user_details = request.get_json()
    email = user_details["email"]
    name = user_details["name"]
    result = event_controller.insert_user(email, name)
    return make_response(jsonify(result), 201)

@app.route("/event_signup", methods=["POST"])
def event_signup():
    user_details = request.get_json()
    event_uid = user_details["event_uid"]
    email = user_details["email"]
    result = event_controller.event_signup(event_uid, email)
    event_info = event_controller.get_event_info(event_uid)
    user_info = event_controller.get_user_info(email)
    send(event_info, user_info)
    return make_response(jsonify(result), 201)

def send(event_info, user_info):
    send_details = {}
    send_details['username'] = json.loads(user_info[0][0]).get("name")
    send_details['email'] = json.loads(user_info[0][0]).get("email")
    send_details.update(json.loads(event_info[0][0]))
    email_invite(send_details)

@app.route("/event_unsign", methods=["DELETE"])
def event_unsign(   ):
    user_details = request.get_json()
    event_uid = user_details["event_uid"]
    email = user_details["email"]
    result = event_controller.event_unsign(event_uid, email)
    return jsonify(result)

"""
Enable CORS. Disable it if you don't need CORS
"""
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*" # <- You can change "*" for a domain for example "http://localhost"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response


if __name__ == "__main__":
    create_event()
    create_user()
    signed_events()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=True)
