import argparse


class KeyValueParseAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_strings=None):
        value_dict = getattr(namespace, self.dest, [])
        if value_dict is None:
            value_dict = {}

        try:
            for value in values:
                k, v = value.split('=')
                value_dict[k] = v
                setattr(namespace, self.dest, value_dict)
        except ValueError as e:
            raise argparse.ArgumentError(self, 'This option takes a space-separated list of key=value pairs as an argument.')
