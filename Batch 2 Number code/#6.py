# Prog06: Subtract all numbers from the first number
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
result = numbers[0] - sum(numbers[1:])
print("Result:", result)