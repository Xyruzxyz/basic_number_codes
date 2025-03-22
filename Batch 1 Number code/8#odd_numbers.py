odd_numbers = 0
for i in range(10):
    num = int(input("Enter an odd number: "))
    if num % 2 !=0: 
        odd_numbers += 1
    print("Total is: ", odd_numbers)
