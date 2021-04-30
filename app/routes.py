from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route('/hello-world', methods = ["GET"])
def get_hello_world():
    my_response = "Hello, World!"
    return my_response

@hello_world_bp.route('/hello-world/JSON', methods = ["GET"])
def hello_world_json():
    return{
        "name":"Abby C",
        "Message":"Hiya!",
        "Hobbies":["Baking", "Coding","Reading"] 
    },201

@hello_world_bp.route('/broken-endpoint-with-broken-server-code')
def broken_endpoint():
    response_body = {
        "name":"Abby C",
        "Message":"Hiya!",
        "Hobbies":["Baking", "Coding","Reading"] 
    }
    new_hobby = "Surfing"
    response_body["Hobbies"].append(new_hobby)
    return response_body