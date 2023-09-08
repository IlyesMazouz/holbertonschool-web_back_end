#!/usr/bin/env python3
"""
a Python script that provides some stats about nginx logs stored in MongoDB
"""
from pymongo import MongoClient

if __name__ == "__main__":
    """
    Database: logs, Collection: nginx
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    log_collection = client.logs.nginx

    total_logs = log_collection.count_documents({})
    print(f"Total logs: {total_logs}")

    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("HTTP Methods:")
    for method in http_methods:
        count = log_collection.count_documents({"method": method})
        print(f"\t{method}: {count}")

    status_check_count = log_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"Total status checks: {status_check_count}")
