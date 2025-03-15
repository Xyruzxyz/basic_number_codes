#Input 10 numbers
#use list comprehension to get the sum of all numbers except the first number
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]
#Subtract all numbers from the first number
result = numbers[0] - sum(numbers[1:])
#print the result
print("Result:", result)