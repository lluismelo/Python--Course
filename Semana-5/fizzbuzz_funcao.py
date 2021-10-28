
def fizzbuzz(num):
    fizz = num % 3
    buzz = num % 5
    if(fizz == 0 and buzz > 0):
        return ("Fizz")
    if (buzz == 0 and fizz>0):
        return ("Buzz")
    if (fizz == 0 and buzz == 0):
        return ("FizzBuzz")
    else:
        return(num)