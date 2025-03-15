# set count to 0
even_number= 0 
#repeat 10 times
for i in range(10):
    #get the input
    num = int(input("Enter a number: "))
    #check if the number is even
    if num%2 == 0:
        #increment the counter
        even_number += 1
        #print even count
print("Even count: ", even_number)     