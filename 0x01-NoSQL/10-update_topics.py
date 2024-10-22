#!/usr/bin/env python3
""" Update MongoDB document using PyMongo
"""


def update_topics(mongo_collection, name, topics):
    """
    Update topics of many documents
    """

    coll = mongo_collection
    coll.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
            )
