# coding: utf-8


from . import CONFIG, NAME
from ..kernel import FUNCTIONS


def get_config():
    """Return the global config dictionary."""
    return CONFIG


def disable_config():
    """Disable config resolution."""
    del FUNCTIONS[NAME]
