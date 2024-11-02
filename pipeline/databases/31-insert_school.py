#!/usr/bin/env python3
""" Implements inser_school
"""


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new document in a collection based
    Args:
        **kwargs: the fields in the document
    Returns:
        (string): the id of the new document
    """
    document = mongo_collection.insert_one(kwargs)
    return (document.inserted_id)
