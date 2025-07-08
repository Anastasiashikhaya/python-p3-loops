#!/usr/bin/env python3

def happy_new_year():
    """Prints numbers from 10 down to 1, then 'Happy New Year!'"""
    for i in range(10, 0, -1):
        print(i)
    print("Happy New Year!")

def square_integers(int_list):
    """Returns a new list with squared integers"""
    return [num ** 2 for num in int_list]

def fizzbuzz():
    """Prints FizzBuzz pattern from 1 to 100"""
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
if __name__ == "__main__":
    print("=== Happy New Year Countdown ===")
    happy_new_year()
    
    print("\n=== Squaring Numbers ===")
    print(square_integers([1, 2, 3, 4, 5]))
    
    print("\n=== FizzBuzz ===")
    fizzbuzz()