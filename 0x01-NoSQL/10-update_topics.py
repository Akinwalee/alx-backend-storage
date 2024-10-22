#!/usr/bin/env python3
""" Update MongoDB document using PyMongo """


def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a document
    """

    coll = mongo_collection
    if not coll.count_documents({}):
        return []
    return ([doc.upserted_id
            for doc in
            coll.update_many({"name": name}, {"$set": "topics": topics})])
