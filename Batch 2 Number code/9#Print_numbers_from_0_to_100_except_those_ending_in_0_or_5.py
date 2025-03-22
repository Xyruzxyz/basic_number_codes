#use for loop to print numbers from 0 to 100 except those ending in 0 or 5
for num in range(101):
#check if the number is not ending in 0 or 5
    if num%5 != 0:
        print(num)
