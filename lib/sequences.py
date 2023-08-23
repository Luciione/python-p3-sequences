def print_fibonacci(length):
    if length == 0:
        print([])  # Print an empty list for length 0
    elif length == 1:
        print([0])  # Print [0] for length 1
    else:
        fibonacci_sequence = [0, 1]  # Initialize the first two Fibonacci numbers
        while len(fibonacci_sequence) < length:
            next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fibonacci)
        print(fibonacci_sequence)
