#!/usr/bin/env python3
""" Implements update_topics
"""


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name
    Args:
        mongo_collection (pymongo): the MongoDB collection to use
        name (string): the school name to update
        topics (list): list of topics approached 
        in the school
    """
    mongo_collection.update_many({'name': name},
                                 {'$set': {'topics': topics}})
