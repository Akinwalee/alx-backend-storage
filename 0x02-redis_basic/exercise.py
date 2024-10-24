#!/usr/bin/env python3
"""
Module for using Redis for caching in python
"""

import uuid
import redis
from typing import Any, Callable, Union


class Cache:
    """
    A class for storing data in Redis
    """
    def __init__(self) -> None:
        '''Initializes a Cache instance
        '''
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores a value in Redis and returns the key
        """
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key