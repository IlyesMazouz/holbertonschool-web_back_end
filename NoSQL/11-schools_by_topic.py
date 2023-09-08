#!/usr/bin/env python3
"""
a Python function that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of schools having a specific topic
    """
    filter_query = {"topics": topic}
    schools = mongo_collection.find(filter_query)
    return list(schools)
