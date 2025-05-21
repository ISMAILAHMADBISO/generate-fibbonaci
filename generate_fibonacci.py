def generate_fibonacci(n):
    """
    Generates the Fibonacci sequence up to n terms.
    :param n: Number of terms to generate in the sequence
    :return: List containing the Fibonacci sequence
    """
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Generate the Fibonacci sequence
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_term)
    
    return fibonacci_sequence

# Prompt the user for input
if __name__ == "__main__":
    print("Welcome to the Fibonacci Sequence Generator!")
    try:
        terms = int(input("Enter the number of terms to generate: "))
        result = generate_fibonacci(terms)
        print(f"The first {terms} terms of the Fibonacci sequence are:")
        print(result)
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
