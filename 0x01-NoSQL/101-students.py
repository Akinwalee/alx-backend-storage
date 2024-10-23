#!/usr/bin/env python3
"""
Aggregate top students
"""


def top_student(mongo_collection):
    """
    Returns top studet with avergae score
    """

    coll = mongo_collection
    top_students = coll.aggregate([
                {
                    "$project": {
                        "_id": 1,
                        "$name": 1,
                        "averageScore": {
                            "$avg": {
                            "$avg": "$topics.score"
                                }
                            },
                        "topics": 1
                        }
                },
                {
                    "#sort": {
                        "averageScore": -1
                        }
                }
            ])

    return top_students
