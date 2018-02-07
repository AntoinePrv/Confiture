# coding: utf-8

"""Set functions for the global config.

This functions are used to set the values in the global config dictionary.
The public interface to modify the configuration are `set_config` and
`update_config`. They have the same signature but the former erase past entries
while the latter updates them. The configuration can be retrieved with
`get_config`.

"""

import pathlib
from . import CONFIG


def set_config(*args, **kwargs):
    """Set the config.

    Set a new value for the module global variable configuration.
    {doctring}
    """.format(doctring=_find_config.__doc__)
    global CONFIG
    CONFIG = _find_config(*args, **kwargs)


def update_config(*args, **kwargs):
    """Update the config.

    Update the module global variable configuration with new values. The udapte
    is to be understood as dictionary updates, so updating existing values and
    adding new ones.
    {doctring}
    """.format(doctring=_find_config.__doc__)
    conf = _find_config(*args, **kwargs)
    CONFIG.update(conf)


def get_config():
    """Return the global config dictionary."""
    return CONFIG


def _find_config(*args, **kwargs):
    """Resolution of parameters.

    - If all parameters are keywords parameters (including no parameters),
    then these key values pairs are used as for the configuration.
    - Otherwise, we expect only one positional argument.
        - if the argument is a dictionnary it is used as is.
        - if the argument is of type `str` (a valid path to a file) or
        `pathlib.Path`, then the values are read from a file. Format is infered
        from extension and include pickle (`.pkl`), json (`.json`) and yaml
        (`.yaml`, `.yml`).

    """
    # the config we want to read
    conf = None

    if len(args) == 0:
        # interpreted as keywords only
        conf = kwargs
    elif len(args) == 1 and len(kwargs) == 0:
        # expect only one argument
        param = args[0]
        if type(param) is dict:
            # simple case of a dictionnary
            conf = param
        elif type(param) is pathlib.Path:
            # otherwise interpreted as a file, we check extensions
            suffix = param.suffix.lower()
            if suffix in (".yaml", ".yml"):
                conf = _config_from_yaml(str(param))
            elif suffix is ".json":
                conf = _config_from_json(str(param))
            elif suffix is ".pkl":
                conf = _config_from_pickle(str(param))
        elif type(param) is str:
            # code reuse - falls in the previous case
            conf = _find_config(pathlib.Path(param))

    if conf is None:
        # no resulution method found
        raise ValueError(f"Invalid input {args}, {kwargs}")
    else:
        return conf


def _config_from_yaml(path):
    """Read config from a yaml file."""
    import yaml
    with open(path) as f:
        return yaml.load(f)


def _config_from_json(path):
    """Read config from a json file."""
    import json
    with open(path) as f:
        return json.load(f)


def _config_from_pickle(path):
    """Read config from a pickle file."""
    import pickle
    return pickle.load(path)


def _config_from_argparse():
    # make use of
    # args, unknown = parser.parse_known_args()
    # needs to define wether we take unknown or not (same as sys.argv so should
    # probalby be another project).
    # If we define config exporter, we can have one to generate args in
    # argparse (for parsing)
    raise NotImplementedError()
