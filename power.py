def large_power(base, exponent):
    result = base ** exponent
    return result > 5000
print(large_power(2, 10))  # Example: 2^10 = 1024, which is not greater than 5000, so it returns False
print(large_power(10, 3))  # Example: 10^3 = 1000, which is not greater than 5000, so it returns False
print(large_power(20, 4))  # Example: 20^4 = 160000, which is greater than 5000, so it returns True