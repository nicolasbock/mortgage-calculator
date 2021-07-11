class Loan(object):

    principal: int
    term: int
    rate: float
    r: float
    payment: float
    amortization: list[float]

    def __init__(self, principal, term, rate):
        """Constructor for a Loan object.

        :param principal: The principal of the loan.
        :param term: The length of the loan in months.
        :param rate: The interest rate of the loan in percent.
        """

        self.principal = principal
        self.term = term
        if rate < 0:
            raise Exception("The rate cannot be negative")
        self.rate_percent = rate
        self.rate = self.rate_percent / 100
        self.r = 1 + self.rate

        if self.rate > 0:
            temp = self.r**self.term
            self.payment = self.principal * self.rate * temp / (temp - 1)
            self.amortization = [
                {
                    "month": i,
                    "interest": 0,
                    "principal": (self.principal * self.r**i
                                  - self.payment * (self.r**i - 1)
                                  / (self.r - 1))
                }
                for i in range(self.term + 1)
            ]
        else:
            self.payment = self.principal / self.term
            self.amortization = [
                {
                    "month": i,
                    "interest": 0,
                    "principal": self.principal - self.payment * i
                }
                for i in range(self.term + 1)]

    @property
    def json(self):
        return {
            "principal": self.principal,
            "term": self.term,
            "rate": self.rate,
            "payments": self.payment,
            "amortization": self.amortization,
        }
