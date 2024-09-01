import argparse
import frontmatter
import os
import sys
from logging import getLogger, basicConfig, INFO


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


def main():
    basicConfig(level = INFO)
    logger = getLogger(__name__)

    parser = argparse.ArgumentParser(description='edit Jekyll-style YAML front matter with values of passed parameters')
    parser.add_argument('file',
                        help='path to the text file containing Jekyll-style YAML front matter')
    parser.add_argument('-o',
                        '--out',
                        help='out file path. if omitted, the original file is overwritten')
    parser.add_argument('-p',
                        '--params',
                        action=KeyValueParseAction,
                        nargs='*',
                        help='space-separated list of key=value pairs')
    args = parser.parse_args()

    try:

        if not args.params:
            logger.info('No parameters found. There are no changes.')
            sys.exit(os.EX_OK)

        post = frontmatter.load(args.file)
        for k, v in args.params.items():
            post[k] = v
        if args.out:
            with open(args.out, 'wb') as o:
                frontmatter.dump(post, o)
            logger.info(f'file saved. path: {args.out}')
        else:
            with open(args.file, 'wb') as f:
                frontmatter.dump(post, f)
            logger.info(f'file saved. path: {args.file}')
    except FileNotFoundError as e:
        logger.error(f"{e.strerror}: '{e.filename}'")
        sys.exit(os.EX_IOERR)


if __name__ == '__main__':
    main()
