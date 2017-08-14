def fizzbuzz():
    cur = 0
    while (cur != 100):
        if cur % 3 == 0 and cur % 5 == 0:
            print ("FizzBuzz")
        elif cur % 3 ==0:
            print ("Fizz")
        elif cur % 5 == 0:
            print ("Buzz")
        cur += 1
fizzbuzz()
