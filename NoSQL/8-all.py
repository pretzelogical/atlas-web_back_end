#!/usr/bin/env python3
""" Lists all documents in a collection """


def list_all(mongo_collection):
    """ Puts all the documents in a collection into a list """
    return list(mongo_collection.find())
