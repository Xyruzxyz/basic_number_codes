odd_numbers = 0
for i in range(10):
    num = int(input(f"{i+1}.  Enter an odd number: "))
    if num % 2 !=0: 
        odd_numbers += 1
    else:
        print("That was not an odd number.")
print(f"You entered {odd_numbers} odd numbers.")