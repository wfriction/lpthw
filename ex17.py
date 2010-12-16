from sys import argv
from os.path import exists

script, from_file, to_file = argv

# we could do these two on one line too, how?
# input = open(from_file)
# indata = input.read()
indata = open(from_file).read()

print indata

print "Copying %d bytes from %s to %s" % (len(indata), from_file, to_file)

# print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
# raw_input("Ready, hit RETURN to continue, CTRL-C to abort.")

# output = open(to_file, 'w')
# output.write(indata)
open(to_file, 'w').write(indata)

print "Alright, all done."

# output.close()
# input.close()
