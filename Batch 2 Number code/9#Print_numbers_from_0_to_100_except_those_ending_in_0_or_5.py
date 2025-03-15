#use for loop to print numbers from 0 to 100 except those ending in 0 or 5
for num in range(101):
#check if the number is not ending in 0 or 5
    if num%10 != 0 and num%10 != 5:
        print(num)