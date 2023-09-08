#!/usr/bin/env python3
"""
a Python function that changes all topics of school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    filter_query = {"name": name}
    update_query = {"$set": {"topics": topics}}
    mongo_collection.update_many(filter_query, update_query)
