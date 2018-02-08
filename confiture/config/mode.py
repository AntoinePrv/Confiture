# coding: utf-8

"""Set the mode the configurations are applied.

FIXME problem with signature of keywords only....

"""

from . import CONFIG


def forced(*params):
    def _forced(func):
        def wrapper(*args, **kwargs):
            # defautls are used in case of conflict
            defaults = {p: CONFIG[p] for p in params if p in CONFIG}
            return func(*args, **{**kwargs, **defaults})
        return wrapper
    return _forced
