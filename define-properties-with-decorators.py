class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100
    
    @property
    def dollars(self):
        return self._cents / 100
    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100

bank_account = Currency(5000)
print(bank_account.dollars)

bank_account = Currency(10000)
print()

    

