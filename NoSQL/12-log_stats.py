#!/usr/bin/env python3
"""
a Python script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def get_logs_collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx
    return collection


def count_documents(collection):
    return collection.count_documents({})


def count_methods(collection):
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {}
    for method in methods:
        count = collection.count_documents({"method": method})
        method_counts[method] = count
    return method_counts


def count_status_check(collection):
    count = collection.count_documents({"method": "GET", "path": "/status"})
    return count


if __name__ == "__main__":
    collection = get_logs_collection()

    total_logs = count_documents(collection)
    print(f"{total_logs} logs")

    print("Methods:")
    method_counts = count_methods(collection)
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")

    status_check_count = count_status_check(collection)
    print(f"{status_check_count} status check")
