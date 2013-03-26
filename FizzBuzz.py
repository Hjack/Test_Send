# FizzBuzz program
# Prints numbers 1-100.  Prints "Fizz" for multiples of 3, "Buzz" for multiples
# of 5 and "FizzBuzz" for multiples of 3 and 5.
x = range(1,101)
for i in x:
    if i % 3 == 0 and i % 5 != 0:
        print "Fizz"
    elif i % 5 == 0 and i % 3 != 0:
        print "Buzz"
    elif i % 3 == 0 and i % 5==0:
        print "FizzBuzz"
    else:
        print i

        
