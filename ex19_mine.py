from sys import argv

script, num1, num2 = argv

num3 = num1 + num2

def add(num1, num2):
    print "The sum of %r and %r is %r." % (num1, num2, num3)

add(num1, num2)

# need to run this 10 different ways
