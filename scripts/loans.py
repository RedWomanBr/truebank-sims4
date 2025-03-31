import logging

# Configure logging
logging.basicConfig(level=logging.INFO)


class Loan:
    def __init__(self, loan_type: str, amount: float, interest_rate: float):
        """
        Initialize a Loan object.

        :param loan_type: Type of the loan (e.g., 'estudantil', 'consignado').
        :param amount: Principal amount of the loan.
        :param interest_rate: Interest rate of the loan.
        """
        self.loan_type = loan_type
        self.amount = amount
        self.interest_rate = interest_rate
        self._balance = amount

    def make_payment(self, payment: float):
        """
        Make a payment to the loan.

        :param payment: Amount to be paid.
        """
        if payment <= 0:
            logging.error("Payment must be greater than zero.")
            return

        if payment > self._balance:
            logging.error("Payment exceeds loan balance.")
            return

        self._balance -= payment
        logging.info(f"Payment of {payment} made. Loan balance: {self._balance}")

    def calculate_interest(self) -> float:
        """
        Calculate the interest on the current balance.

        :return: Calculated interest.
        """
        return self._balance * self.interest_rate

    @property
    def balance(self) -> float:
        """Get the current balance of the loan."""
        return self._balance


class ConsignedLoan(Loan):
    def __init__(self, amount: float, interest_rate: float, employer: str):
        """
        Initialize a ConsignedLoan object.

        :param amount: Principal amount of the loan.
        :param interest_rate: Interest rate of the loan.
        :param employer: Employer associated with the consigned loan.
        """
        super().__init__("consignado", amount, interest_rate)
        self.employer = employer


# Example usage
if __name__ == "__main__":
    emprestimo = Loan("estudantil", 500, 0.05)
    emprestimo.make_payment(50)
    logging.info(f"Interest: {emprestimo.calculate_interest()}")

    emprestimo_consignado = ConsignedLoan(1000, 0.03, "Empresa X")
    emprestimo_consignado.make_payment(100)
    logging.info(f"Interest: {emprestimo_consignado.calculate_interest()}")
