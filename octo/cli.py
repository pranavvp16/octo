from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('name', help='The name of the repository')
parser.add_argument('--private', help='Make the repository private', action='store_true')
parser.add_argument('--description', help='The repository description')
