from app import db
from flask import jsonify, Blueprint, Response, request
from app.models.book import Book


books_bp = Blueprint("books", __name__, url_prefix="/books")


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
    elif request.method == "POST":
        request_body = request.get_json()
        new_book = Book(title = request_body["title"],
                        description = request_body["description"]
                                                    )
        db.session.add(new_book)
        db.session.commit()
        
        return (f'book #{new_book.title} has been created', 201 )

@books_bp.route("/<book_id>", methods=["GET","PUT"])
def book(book_id):
    book = Book.query.get(book_id)

    if request.method == "GET":
        return ({
            "id": book.id,
            "title": book.title,
            "description": book.description
        }, 200)
    #else
    request_body = request.get_json()
    try:
        book.title = request_body["title"]
        book.description = request_body["description"]
        # save action
        # db.session.add(book)
        db.session.commit() 
        return ({
                "id": book.id,
                "title": book.title,
                "description": book.description
            }, 200)
    except KeyError:
        return { 
            "message":"Request requires both 'title' and 'description"
        }, 400 