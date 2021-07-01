from mortgage_calculator.parse_commandline import parse_commandline
from mortgage_calculator.loan import Loan


def main():
    options = parse_commandline()
    loan: Loan = Loan(principal=options.principal, term=options.term,
                      rate=options.rate)


if __name__ == "__main__":
    main()
