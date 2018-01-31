# coding: utf-8

"""Defaults configurations."""

from functools import wraps

FUNCTIONS = {}


def identity(*args, **kwargs):
    def _identity(func):
        return func
    return _identity


def runtime_decorator(name):
    def decorator_params(*dec_args, **dec_kwargs):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                new_func = FUNCTIONS.get(name, identity)
                return new_func(*dec_args, **dec_kwargs)(func)(*args, **kwargs)
            return wrapper
        return decorator
    return decorator_params
