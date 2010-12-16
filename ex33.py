def add_and_print_integers_to_array(maxvalue, increment):
    numbers = []

    for i in range(0, maxvalue):
        print "At the beginning, i = %d" % i
        numbers.append(i)
        
        i = i + increment - 1
        print "Updated array:", numbers
        print "End of the for, i = %d" % i
    
    print "The numbers: "

    for num in numbers:
        print num
