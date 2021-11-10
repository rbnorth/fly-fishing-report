# list of flags
#   list rivers
#   set a location
#   create text file
#   create mp3 
#   upload to s3
#   do not print to screen
#   help

from argparse import Action, ArgumentParser

def parser():
    parser = ArgumentParser(allow_abbrev=False, description='Get fly fishing river reports in Southwest Montana')
    parser.add_argument('-p', '--profile',
        type=str,
        #required=True,
        help="sets aws profile - aws configure list-profiles")
    parser.add_argument('-l',  '--list',
        action='store_true',
        help="List of SW Montana rivers")
    parser.add_argument('-L', '--location',
        help="Set river location")

    return parser