# coding: utf-8

from . import CONFIG, enable_config


class Configure(object):

    def __init__(self, config):
        """Initialize Config."""
        self.__config = config
        self.__mode = None

    def mode(self, new_mode):
        """Change mode."""
        return self.__class__(self.__config, new_mode)

    def set(self):
        """Set as new configuration."""
        global CONFIG
        CONFIG = self.__config
        if self.__mode is not None:
            raise NotImplementedError()
        else:
            # We need to set a default mode here
            raise NotImplementedError()

    def update(self):
        """Update the configuration with these values."""
        CONFIG.update(self.__config)
        if self.__mode is not None:
            raise NotImplementedError()

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
