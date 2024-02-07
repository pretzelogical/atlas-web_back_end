#!/usr/bin/env python3
""" Redis cache """
from redis import Redis
from typing import Union, Callable
from functools import wraps
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
        Counts calls of a function and store in db as the methods __qualname__
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """ Wrapper function """
        key = method.__qualname__
        redis = Redis()
        redis.incr(key)
        return method(*args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
        Stores the history of inputs and outputs
        in method.__qualname:inputs/outputs
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """ Wrapper function """
        key = method.__qualname__
        redis = Redis()
        input_args = str(args[1:])
        redis.rpush(f"{key}:inputs", input_args)
        output = method(*args, **kwargs)
        redis.rpush(f"{key}:outputs", output)
        return output
    return wrapper


def replay(method: Callable):
    """
        Displays the history of calls of a particular function
    """
    name = method.__qualname__
    redis = Redis()
    inputs = redis.lrange(f"{name}:inputs", 0, -1)
    outputs = redis.lrange(f"{name}:outputs", 0, -1)
    print(f"{name} was called {redis.get(name).decode('utf-8')} times:")
    for func_input, func_output in zip(inputs, outputs):
        func_input = func_input.decode('utf-8')
        func_output = func_output.decode('utf-8')
        print(f"{name}(*{func_input}) -> {func_output}")


class Cache:
    """ Cache that connects to a redis instance """

    def __init__(self):
        """ Initialize redis connection """
        self._redis = Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Takes data and stores it in the cache with
            an auto generated key
        """
        key_name = str(uuid4())
        self._redis.set(key_name, data)
        return key_name

    def get(self, key: str, fn: Callable = None):
        """
            Gets data and retrieves it from the cache optionally
            converting the returned value using fn
        """
        res = self._redis.get(key)
        if fn is not None:
            return fn(res)
        return res

    def get_str(self, key: str) -> str:
        """ Call self.get() with str as converter """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Call self.get() with int as converter """
        return self.get(key, int)
