import argparse
from constants.info import DESCRIPTION, VERSION, ASCII_ART
import os

parser = argparse.ArgumentParser(
    description=DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=ASCII_ART,
    prog='octo'
)

parser.add_argument(
    '-v', '--version',
    action='version',
    version=f'%(prog)s {VERSION}'
)

init_parser = parser.add_argument(
    'init',
    help='Initialize the project'
)
init_parser.
args = parser.parse_args()
print(args.init)

