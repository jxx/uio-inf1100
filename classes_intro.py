class Account:
#Konstruktor __init__ er en spesialmetode som python kaller nar vi instansierer et objekt
   def __init__(self, name, account_number, initial_amount):
       # store input into variables
       # _ prefix for private variables. Only naming convention, not builtin
       self._name = name
       self._no = account_number
       #self.balance = initial_amount
       self._transactions = [initial_amount]

   def deposit(self, amount):
       #self.balance += amount
       self._transactions.append(amount)

   def withdraw(self, amount):
       #self.balance -= amount
       self._transactions.append(-amount)

   def dump(self):
       s = '%s, %s, balance: %s' % \
           (self._name, self._account_number, self._balance)
       print s
   
   def print_transactions(self):
       print self._transactions

   def __str__(self):
       # overrides defult text representatio of object
       return self.dump()

   def getbalance(self):
       #return self.balance
       return sum(self._transactions)

a = Account("Per", "1234567890", 0.0)

a.deposit(200)

#a.print_transactions()

print a
