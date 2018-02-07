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
TODO: make a hyerachical naming convention in the config
TODO: read from multiple configs and merge them
TODO: do one that apply params but softly aka, after the given arguments, even
    if positional probably needs inspection of function

NEW NAME: aposteriori
"""

from .. import kernel as ker


CONFIG = {}
NAME = __name__

config = ker.runtime_decorator(NAME)
