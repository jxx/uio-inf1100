#print '7.10 Hello'

class Hello:
    #No constructior as class is called without any arguments

    def __call__(self, text):
        return "Hello, %s!" % text

    def __str__(self):
        return 'Hello, World!'

a = Hello()
print a('Students') # looks like a function
print(a)            # actually: str(a) -> a.__str__()
