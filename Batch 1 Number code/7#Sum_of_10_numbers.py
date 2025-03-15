#Sum of 10 numbers
total = 0
for i in range(10):
    num = float(input(f"{i + 1}. Enter a number: "))
    total += num
    print("The sum of 10 numbers is:", total)  