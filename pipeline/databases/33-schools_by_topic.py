#!/usr/bin/env python3
""" Implements schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """ Finds list of all schools with a specific topic
    Args:
        mongo_collection: the MongoDB collection to use
        topic(string): the topic to search for

    returns:
        (list): schools with the given topic
    """
    schools = []
    documents = mongo_collection.find({'topics': {'$all': [topic]}})
    for doc in documents:
        schools.append(doc)
    return schools
