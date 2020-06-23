
from celery.utils.log import get_task_logger
from src import celery, app, mongo

@celery.task()
def insert_book(book):
    mongo.db.books.insert_one(book)

@celery.task()
def empty_bookshelf():
    mongo.db.books.remove()

def get_books():
    cursor = mongo.db.books.find({})
    return [filter_id(book) for book in cursor]

def filter_id(document):
    """Filter the id of the mongo document and returns a Python dictionary

    Args:
        document (dict): Mongo document as python dictionary

    Returns:
        dict: Dictionary with all the attributes of the document except _id
    """
    n = document.copy()
    n.pop('_id',None)
    return n