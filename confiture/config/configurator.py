# coding: utf-8

"""Configurator module.

Aims at configuring the values in the global config of the module `config` as
well as how they are used.

"""

from .config import _get_config, _set_config, _set_resolve
from . import resolver


class Configure(object):
    """Configure class.

    The class is used to define a behaviour for the module `config`. The class
    is used in a imutable fashion, returning new objects.
    The class is lazy and doesn't change anything until a action method is
    called, namely
        - `set` sets the global configuration erasing previous behaviour.
        - `update` only updates the global configuration with new information
        leaving other states unchanged.

    Attributes
    ----------
    __config : dict
        Holds a configuration ready to be pushed to the module level
        configuration.
    __mode : str
        Mode is the way the module decorator apply the values of the
        global configuration to other functions.

    """

    __modes_to_resolver = {
        "defaults": resolver.defaults_changer,
        "override": resolver.signature_changer
    }

    @classmethod
    def _avail_modes(klass):
        return klass.__modes_to_resolver.keys()

    @classmethod
    def _resolve_mode(klass, mode):
        return klass.__modes_to_resolver.get(mode, resolver.defaults_changer)

    def __init__(self, config, mode=None):
        """Initialize Config."""
        self.__config = config
        available_modes = Configure._avail_modes()
        if mode is not None and mode not in available_modes:
            raise ValueError(f"Undefined mode: {mode}.\n"
                             f"Use one of {available_modes}.")
        else:
            self.__mode = mode

    def mode(self, new_mode):
        """Change mode."""
        return Configure(self.__config, new_mode)

    def set(self):
        """Set as new configuration."""
        _set_config(self.__config)
        _set_resolve(Configure._resolve_mode(self.__mode))

    def update(self):
        """Update the configuration with these values."""
        _get_config().update(self.__config)
        if self.__mode is not None:
            _set_resolve(Configure._resolve_mode(self.__mode))

    @classmethod
    def from_kwargs(klass, **kwargs):
        """Read config from keywords arguements."""
        return klass(config=kwargs)

    @classmethod
    def from_yaml(klass, path):
        """Read config from a yaml file."""
        import yaml
        with open(path) as f:
            config = yaml.load(f)
        return klass(config=config)

    @classmethod
    def from_json(klass, path):
        """Read config from a json file."""
        import json
        with open(path) as f:
            config = json.load(f)
        return klass(config=config)

    @classmethod
    def from_pickle(klass, path):
        """Read config from a pickle file."""
        import pickle
        config = pickle.load(path)
        return klass(config=config)

    @classmethod
    def from_args(klass):
        """Read config from command line arguments."""
        # make use of
        # args, unknown = parser.parse_known_args()
        # needs to define wether we take unknown or not (same as sys.argv so
        # should probalby be another project).
        # If we define config exporter, we can have one to generate args in
        # argparse (for parsing)
        raise NotImplementedError()
