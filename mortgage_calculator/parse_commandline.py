import argparse


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--principal",
        metavar="P",
        type=int,
        help="The principal of the mortgage",
        default=0)
    options = parser.parse_args()
    options.principal = int(options.principal)
    return options
