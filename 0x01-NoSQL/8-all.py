#!/usr/bin/env python3
""" List all documents in a modgodb database collection """


def list_all(mongo_collection):
    """
    List all documents in a collection
    return [] if collection si empty
    """

    coll = mongo_collection.find()
    if not len(coll):
        return []
    for doc in coll:
        print(doc)
