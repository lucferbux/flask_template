from src import app
from flask import request, jsonify, make_response, request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from .utils.util import insert_book, get_books, empty_bookshelf
from .exceptions.exceptions import EmptyBody
from .model.dataclasses import Book

@app.route('/api/bookshelf', methods=['GET'])
@jwt_required
def scan():
    """API endpoint that retrieves all the books in the bookshelf

    Returns:
        dict: List with the books
    """
    books = get_books()
    
    return jsonify({200: books})


@app.route('/api/insert', methods=['POST'])
@jwt_required
def insert():
    """Insert a new book

    Returns:
        200: JSon response
    """
    body = request.json
    if(body):
        try:
            book = Book(**body)
            insert_book.delay(book.get_dict())
        except Exception as e:
            app.logger.error(f"Error in parsing body: {e}")
            return jsonify({400: "Body error"})

    return jsonify({200: "OK"})

@app.route('/api/delete', methods=['DELETE'])
@jwt_required
def delete():
    """Deletes the bookshelf

    Returns:
        200: JSon response
    """
    try:
        empty_bookshelf.delay()
    except Exception as e:
        app.logger.error(f"Error removing the bookshelf: {e}")
        return jsonify({400: "Error removing"})

    return jsonify({200: "OK"})