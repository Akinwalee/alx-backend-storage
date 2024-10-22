#!/usr/bin/env python3
"""
Find Schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns schools by topic
    """

    coll = mongo_collection
    return [school for school in coll.find({"topic": topic})]
