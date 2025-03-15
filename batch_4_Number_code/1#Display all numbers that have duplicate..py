#Input 10 numbers
#Initialize list
num_list = []
#Keep asking user input
[int(input(f"Enter number {i+1}: ")) for i in range(10)]
#Display all numbers that have duplicate
print("Numbers that have duplicates:", [num for num in num_list if num_list.count(num) > 1])
#Display all numbers
print("All numbers:", num_list)

        
   
