def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))

    prime_numbers = generate_primes(start_range, end_range)
    print("Prime numbers in the specified range:", prime_numbers)
