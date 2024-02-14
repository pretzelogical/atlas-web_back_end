#!/usr/bin/env python3
""" Returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Returns the list of school having a specific topic """
    if not isinstance(topic, list):
        topic = [topic]
    return list(mongo_collection.find({"topics": {"$in": topic}}))
