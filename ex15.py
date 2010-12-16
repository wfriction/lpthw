# import the argument module
from sys import argv

# split the arguments received to the script and filename variables
script, filename = argv

# store the open file in the variable txt
txt = open(filename)

# print the name of the file
print "Here's your file %r:" % filename
# print the contents of the file using the read function of the txt object
print txt.read()


print "I'll also ask you to type it again:"
# get the name of the file again from the user
file_again = raw_input("> ")

# store the open file in the variable txt_again
txt_again = open(file_again, 'w')

txt_again.write(raw_input("What shall I write?\n"))

txt_again.close()

txt_again = open(file_again)

# print the contents of the file contained in txt_again
print txt_again.read()

txt.close()
txt_again.close
