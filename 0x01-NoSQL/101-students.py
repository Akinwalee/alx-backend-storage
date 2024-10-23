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
                    "$unwind": "$topics"
                },
                {
                    "$group": {
                        "_id": "$_iid",
                        "$name": {"$first": "$name"},
                        "averageScore": {"$avg": "$topics.score"}
                        }
                },
                {
                    "#sort": {
                        "averageScore": -1
                        }
                }
            ])

    return list(top_students)
