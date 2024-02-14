#!/usr/bin/env python3
""" Gets stats about Nginx logs store in MongoDB """
from pymongo import MongoClient


client = MongoClient("localhost", 27017)
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

print(f"{client.logs.nginx.count_documents({})} logs")
print("Methods:")
for method in methods:
    num_method = client.logs.nginx.count_documents({"method": method})
    print(f"\t method {method}: {num_method}")
status_check = client.logs.nginx.count_documents(
    {"method": "GET", "path": "/status"}
    )
print(f"{status_check} status check")
