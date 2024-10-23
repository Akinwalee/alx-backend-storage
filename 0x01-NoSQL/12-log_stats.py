#!/usr/bin/env python3
"""
Calculate the stats of the logs in Mongodb
"""


from pymongo import MongoClient


def get_stats():
    """
    Get the stats of logs
    """

    with MongoClient() as client:
        db = client.logs

        x = db.nginx.count_documents({})
        print("{} logs".format(x))
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print("Methods:")
        for method in methods:
            n = db.nginx.count_documents({"method": method})
            print("\tmethod {}: {}".format(method, n))

        stat = db.nginx.count_documents({"method": "GET", "path": "/status"})
        print("{} status check".format(stat))


if __name__ == "__main__":
    get_stats()
