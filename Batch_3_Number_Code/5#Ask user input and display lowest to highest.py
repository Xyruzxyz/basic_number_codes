#Initialize list
num_list2 = []
#Keep asking user input
while True:
    try:
        num_list2.append(int(input("Enter a number: "))) #ask user input
    except ValueError: #If user input is not a number
        print("Invalid input")
        break
    #Display highest to lowest number
    print("Highest to lowest number:", sorted(num_list2, reverse=True))