#get two inputs
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
#Print all numbers between the two inputs
if num1 > num2: #swap numbers if num1 is greater than num2
    num1, num2 = num2, num1 #swap numbers
for number in range(num1 + 1, num2): #loop through numbers between num1 and num2
    print(number) #print number