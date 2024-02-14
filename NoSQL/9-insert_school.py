#!/usr/bin/python3
""" Function insert_school this inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a new_document in a collection based on kwargs """
    res = mongo_collection.insert_one(kwargs)
    return str(res.inserted_id)
