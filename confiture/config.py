# coding: utf-8

"""Confiture for parameters injection.

Uses a Yaml file to define configuration of parameters.
A decorator provides a way to use configuration values before default values.

TODO: figure out the conflict between named entities and positional
    using funciton inspection ?
TODO: provide a dry-run to populate the config file from all default values.
TODO: make a mode to populate the configuration file
TODO: make function call that apply to every function paramter: @config ou @config(True)
TODO: make an identity decorator to deactivate the module
TODO: make one to read from argparse
"""

import yaml
from . import kernel as ker


# defaults = {p: CONFIG[p] for p in params if p in CONFIG}
# func(*args, **{**defaults, **kwargs})

config = ker.runtime_decorator("config")


def set_config(path: str):
    """Read config from yaml file."""
    with open(path) as f:
        conf = yaml.load(f)

    def forced(*params):
        def _forced(func):
            def wrapper(*args, **kwargs):
                defaults = {p: conf[p] for p in params if p in conf}
                return func(*args, **{**kwargs, **defaults})
            return wrapper
        return _forced

    ker.FUNCTIONS["config"] = forced
