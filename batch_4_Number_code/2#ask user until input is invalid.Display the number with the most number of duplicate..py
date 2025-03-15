#Initialize list
num_list = []
#Keep asking user input
while True:
    try:
        num_list.append(int(input("Enter a number: "))) #ask user input until invalid
    except ValueError: #If user input is not a number
        print("Invalid input")
        break
    #Display the number with the most number of duplicate
    print("Most number of duplicate:", max(num_list, key = num_list.count))
        
