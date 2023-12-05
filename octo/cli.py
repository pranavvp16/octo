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
parser.add_argument(
    'auth',
    help = "Authenticate the user with Mindsdb",
    action='store_true'
)

parser.add_argument(
    'init',
    help='Initialize the project'
)

args = parser.parse_args()
if args.auth:
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    print("Authenticating user")

