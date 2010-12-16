def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# print for 20 cheese and 30 crackers
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# print stuff for 10 cheese and 50 crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# print stuff for 30 cheese and 11 crackers
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# add 100 to cheese (10) and add 1000 to crackers (50), then print the top stuff
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
