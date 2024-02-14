#!/usr/bin/env python3
""" Gets stats about Nginx logs store in MongoDB """
from pymongo import MongoClient


def log_clients():
    """ Gets stats about Nginx logs stored in MongoDB """
    client = MongoClient("localhost", 27017)
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{client.logs.nginx.count_documents({})} logs")
    print("Methods:")
    for method in methods:
        num_method = client.logs.nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {num_method}")
    status_check = client.logs.nginx.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_clients()
