#Initialize list
num_list1 = []
#Keep asking user input
while True:
    try:
        num_list1.append(int(input("Enter a number: "))) #ask user input
    except ValueError: #If user input is not a number
        print("Invalid input")
        break
    #Display lowest number
    print("Lowest number:", min(num_list1))
   

