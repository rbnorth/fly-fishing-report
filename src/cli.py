# list of flags
#   list locations
#   location
#   list rivers
#   river
#   create text file
#   create mp3 
#   upload to s3
#   do not print to screen
#   help

from argparse import Action, ArgumentParser

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('-l',  '--list',
            help="List of locations")
    parser.add_argument('-L', '--location',
            help="Set location",
            required=True)
    parser.add_argument()

    return parser