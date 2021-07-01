class Loan(object):

    principal: int
    term: int
    rate: float

    def __init__(self, principal=None, term=None, rate=None):

        self.principal = principal
        self.term = term
        self.rate = rate
