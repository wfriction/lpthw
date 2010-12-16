# import the argument module
from sys import argv

# split the received arguments to python into script (filename) and an input_file
script, input_file = argv

# define the fn print_all which takes the argument f
def print_all(f):
# print the contents of the file f
    print f.read()

# define the fn that goes to the beginning of the file f
def rewind(f):
# go to the byte position 0 in the file f
    f.seek(0)

# define the function that prints a given line, which is passed the line to read and the filename
def print_a_line(line_count, f):
# print the line number and then the contents of that line given from the file f
    print line_count, f.readline()

# open the input file that was passed to the script
current_file = open(input_file)

print "First let's print the whole file:\n"

# use the print_all function on the open file
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# go to the byte position 0 of the file using the rewind function
rewind(current_file)

print "Let's print three lines:"

# set current line as 1
current_line = 1
# use the print a line function to print the first line of the file
print_a_line(current_line, current_file)

# increase the value of current_line by 1 (now 2)
current_line += 1
# print the 2nd line
print_a_line(current_line, current_file)

# print the 3rd line (current line = 3)
current_line += 1
print_a_line(current_line, current_file)
