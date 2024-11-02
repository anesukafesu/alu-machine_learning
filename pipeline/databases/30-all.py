#!/usr/bin/env python3
"""
Implements list_all
"""

def list_all(mongo_collection):
    """ Lists all documents in given MongoDB collection
    Args:
        mongo_collection (Mongo.Collection): the collection
    Returns:
        (list) All the documents or 0 if there are no
        documents
    """
    all_docs = []
    collection = mongo_collection.find()
    for document in collection:
        all_docs.append(document)
    return all_docs
