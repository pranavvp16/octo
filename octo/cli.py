import argparse
from constants.info import DESCRIPTION, VERSION, ASCII_ART
from getpass import getpass
import keyring


def save_password(email, password):
    # Set the password in the keyring
    keyring.set_password(service_name="Octo", username=email, password=password)


parser = argparse.ArgumentParser(
    description=DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    prog="octo",
)

parser.add_argument(
    "-v", "--version", action="version", version=ASCII_ART.format(VERSION)
)
parser.add_argument(
    "auth", help="Authenticate the user with Mindsdb", action="store_true"
)

parser.add_argument("init", help="Initialize the project")

args = parser.parse_args()

if args.auth:
    email = input("Enter your email: ")
    password = getpass(f"Enter password for {email}: ")

    # Save the password using keyring
    save_password(email, password)
    print(f"Password successfully set for {email}")
    # You can add additional authentication logic here if needed

elif args.init:
    # Add logic for project initialization here
    print("Initializing the project")
