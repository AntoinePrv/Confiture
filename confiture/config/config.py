# coding: utf-8

"""Config module for parameters injection.

Defines the behaviour for the runtime decorator associated with this module.

Variables
---------
CONFIG : dict
    The global dictionary of key-values used to resolve parameters.
config : func
    Decorator managed by the kernel module. Will call the a runtime decorator
    to define the resolution of the configuration parameters with the function
    parameters.

Warnings
--------
Do not import CONFIG directly as it reference might be changed later on.

"""

from .. import kernel as ker


CONFIG = {}

config = ker.runtime_decorator(__name__)


# Module management functions.

def _get_config():
    """Return the reference to the global config dictionary."""
    return CONFIG


def _set_config(config):
    """Set a new object for the global config."""
    global CONFIG
    CONFIG = config


def _disable_resolve():
    """Disable config resolution."""
    del ker.FUNCTIONS[__name__]


def _set_resolve(func):
    """Enable the config resolution."""
    ker.FUNCTIONS[__name__] = func


# User friendly functions.

def disable():
    """Disable config resolution."""
    _disable_resolve()


def config_lookup(*keys):
    """Return a copy of the global config, sliced by the given parameters.

    Keys not in the config are ignored.
    """
    return {k: CONFIG[k] for k in set(keys) & CONFIG.keys()}
