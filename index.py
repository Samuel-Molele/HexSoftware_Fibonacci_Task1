def fibonacci(n):
    # Initialize first two Fibonacci numbers
    a = 0
    b = 1
    # If n is 1, print only the first number
    if n == 1:
        print(a)
    # For n > 1, print first two numbers
    else:
        print(a)
        print(b)
    # Generate and print the remaining Fibonacci numbers up to n terms
    for i in range(2,n):
        c = a + b
        a = b 
        b = c
        print(c)
 # Call function to print first 10 Fibonacci numbers       
fibonacci(10)