# coding: utf-8

"""Confiture for parameters injection.

Uses a Yaml file to define configuration of parameters.
A decorator provides a way to use configuration values before default values.

TODO: figure out the conflict between named entities and positional
    using funciton inspection ?
TODO: provide a dry-run to populate the config file from all default values.
"""

import yaml

CONFIG = {}


def set_config(path: str):
    """Read config from yaml file."""
    global CONFIG
    with open(path) as f:
        CONFIG = yaml.load(f)


def config(*params):
    """Functional decorator to inject parameters."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            defaults = {p: CONFIG[p] for p in params if p in CONFIG}
            return func(*args, **{**defaults, **kwargs})
        return wrapper
    return decorator
