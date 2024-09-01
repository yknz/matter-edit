
import argparse
import frontmatter
import os
import sys
from logging import getLogger, basicConfig, INFO


def main():
    basicConfig(level = INFO)
    logger = getLogger(__name__)

    parser = argparse.ArgumentParser(description='select value from Jekyll-style YAML front matter with value of passed parameter')
    parser.add_argument('file',
                        help='path to the text file containing Jekyll-style YAML front matter')
    parser.add_argument('-p',
                        '--param',
                        help='search value')
    args = parser.parse_args()

    try:
        post = frontmatter.load(args.file)

        if not args.param:
            print(post.metadata)
        else:
            print(post[args.param])
    except FileNotFoundError as e:
        logger.error(f"{e.strerror}: '{e.filename}'")
        sys.exit(os.EX_IOERR)


if __name__ == '__main__':
    main()
