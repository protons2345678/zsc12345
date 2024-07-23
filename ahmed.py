def Fibonacci(n):
    if n <= 0:
        return None # invalid input, assuming n should be positive
    # initilize the First two Fibounacci numbers 
    a, b = 0, 1
    # If n is 1 or 2, return the respective Fibounacci number directly
    if n == 1:
        return a
    elif n == 2:
        return b
    
    # Iterate to calculate the nth Fibounacci number
    for _ in range(2, n):
        # calculate the next Fibounacci number 
        a, b = b, a + b

    # After the loop, 'b' will hold the nth Fibounacci number
    return b 

# Example usage:
print(Fibonacci(5)) # Output: 3
print(Fibonacci(10)) # Output: 34
