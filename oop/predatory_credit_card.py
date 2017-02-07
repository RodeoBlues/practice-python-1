from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):
    """ An extension to CreditCard that compounds interest and fees. """

    def __init__(self, customer, bank, acnt, limit, apr):
        """ Create a new predatory credit card instance.

        The initial balance is zero.

        customer    the name of the customer (e.g., 'John Bowman')
        bank        the name of the bank (e.g., 'California Savings')
        acnt        the account identifier (e.g., '5391 0375 9387 5309')
        limit       credit limit (measured in dollars)
        apr         annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)   # call super constructor
        self._apr = apr

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        success = super().charge(price) # call inherited method
        if not success:
            self._balance += 5          # assess penalty
        return success

    def process_month(self):
        """ Assess monthly interest on outstanding balance. """
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor

if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500, 0.0825))

    for val in range(1, 17):
        wallet[0].charge(val)

    for c in wallet:
        print('Customer = ', c.get_customer())
        print('Bank = ', c.get_bank())
        print('Account = ', c.get_account())
        print('Limit = ', c.get_limit())
        print('Balance = ', c.get_balance())
        while c.get_balance() > 100:
            c.make_payment(100)
            print('New balance = ', c.get_balance())
        c.process_month()
        print('Process Month = ', c.get_balance())

