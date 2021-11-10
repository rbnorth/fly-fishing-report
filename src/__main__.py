
import cli
import requests 

from bs4 import BeautifulSoup
from datetime import date

def main():

    # Executes cli.py to parse out
    args = cli.parser().parse_args()

    profile = args.profile
    list_rivers = args.list

    


if __name__ == "__main__":
    main()