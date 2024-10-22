#!/usr/bin/env python3
""" Inserta document in Mongodb using PyMongo """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document in a collection
    Returns the new id
    """

    coll = mongo_collection
    new_doc = coll.insert_one(kwargs)
    return (new_doc.inserted_id)
