import argparse
import frontmatter
import os
import sys
from logging import getLogger, basicConfig, INFO

from .parse_action import KeyValueParseAction


basicConfig(level = INFO)
logger = getLogger(__name__)

parser = argparse.ArgumentParser(description='edit Jekyll-style YAML front matter with values of passed parameters')
subparsers = parser.add_subparsers(dest='command')

show_parser = subparsers.add_parser('show', help='show front matter value')
show_parser.add_argument('file', help='path to the text file containing Jekyll-style YAML front matter')
show_parser.add_argument('-p', '--param', help='search value')

update_parser = subparsers.add_parser('update', help='update front matter value')
update_parser.add_argument('file', help='path to the text file containing Jekyll-style YAML front matter')
update_parser.add_argument('-o', '--out', help='out file path. if omitted, the original file is overwritten')
update_parser.add_argument('-p', '--params', action=KeyValueParseAction, nargs='*', help='space-separated list of key=value pairs')


def main():
    args = parser.parse_args()

    try:
        if args.command == 'show':
            post = frontmatter.load(args.file)
            if not args.param:
                print(post.metadata)
            else:
                print(post[args.param])

        elif args.command == 'update':
            post = frontmatter.load(args.file)
            if not args.params:
                logger.info('No parameters found. There are no changes.')
                sys.exit(os.EX_OK)
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
