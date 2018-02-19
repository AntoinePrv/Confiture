# coding: utf-8

"""Set the mode the configurations are applied."""

from inspect import signature
from functools import partial
from .config import config_lookup


def default_params(func):
    return [name for name, param in signature(func).parameters.items()
            if param.default != param.empty]


def defaults_changer(*params):
    def decorator(func):
        default_params_ = default_params(func)
        for p in params:
            if p not in default_params_:
                raise ValueError(f"Decorator parameter {p} not a default "
                                 f"parameter for function {func}.")

        def wrapper(*args, **kwargs):
            sig = signature(func)
            # parameters given at function call (positional or keyword)
            all_args_keys = sig.bind(*args, **kwargs).arguments.keys()
            # parameters that we need to resolve:
            # all the params in the decorator minus the ones given to the
            # function call
            params_left = set(params) - all_args_keys
            return func(*args, **{**config_lookup(*params_left), **kwargs})

        return wrapper
    return decorator


def signature_changer(*params):
    def decorator(func):
        config = config_lookup(*params)
        func_params = signature(func).parameters.keys()
        for p in params:
            if p not in func_params:
                raise ValueError(f"Decorator parameter {p} is not a valid "
                                 f"parameter for function {func}.")
            if p not in config:
                raise ValueError(f"Decorator parameter {p} is not available "
                                 "in the configuration.")

        return partial(func, **config_lookup(*params))
    return decorator
