import argparse
import re


term_unit_re = re.compile(r"^([0-9]+)(y(ears)?|m(onths)?)?$")


def parse_commandline():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--principal",
        metavar="P",
        type=int,
        help="The principal of the mortgage",
        default=0)
    parser.add_argument(
        "--term",
        metavar="T",
        type=str,
        help="The term of the loan, T, optionally with a unit "
        "('m'onths, 'y'ears). Default unit is years.",
        default="30y")
    options = parser.parse_args()
    options.principal = int(options.principal)
    result = term_unit_re.search(options.term)
    if result:
        multiplier = 1
        if result.group(2):
            if result.group(2)[0] == 'y':
                multiplier = 12
        options.term = multiplier * int(result.group(1))
    else:
        raise Exception("cannot parse term '{}'".format(options.term))
    return options
