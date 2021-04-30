from app import db
from flask import jsonify
from flask import Blueprint
from flask import request
from .models.book import Book


books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book = Book.query.get(book_id)

    if book:
        return ({
            "id": book.id,
            "title": book.title,
            "description": book.description
        }, 200)
    return{
        "message": f"Book {book_id} not found",
        "success": False,
        }, 404

@books_bp.route("",methods=["POST","GET"])
def books():
    if request.method == "GET":
        books = Book.query.all()
        books_response = []
        for book in books:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
        return jsonify(books_response), 200
    else:
        request_body = request.get_json()
        new_book = Book(title = request_body["title"],
                        description = request_body["description"]
                                                    )
        db.session.add(new_book)
        db.session.commit()
        
        return (f'book #{new_book.title} has been created', 201 )

# hello_world_bp = Blueprint("hello_world", __name__)
# @hello_world_bp.route('/hello-world', methods = ["GET"])
# def get_hello_world():
#     my_response = "Hello, World!"
#     return my_response

# @hello_world_bp.route('/hello-world/JSON', methods = ["GET"])
# def hello_world_json():
#     return{
#         "name":"Abby C",
#         "Message":"Hiya!",
#         "Hobbies":["Baking", "Coding","Reading"] 
#     },201

# @hello_world_bp.route('/broken-endpoint-with-broken-server-code')
# def broken_endpoint():
#     response_body = {
#         "name":"Abby C",
#         "Message":"Hiya!",
#         "Hobbies":["Baking", "Coding","Reading"] 
#     }
#     new_hobby = "Surfing"
#     response_body["Hobbies"].append(new_hobby)
#     return response_body
