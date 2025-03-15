#Initialize list
filtered_numbers = []
#Keep asking user to input
while True:
    try:
        #ask user input
        num = int(input("Enter a number: "))
        #Display unique if not duplicate, else print duplicate
        print("Duplicate" if num in filtered_numbers else "Unique")
        filtered_numbers.append(num)
    except ValueError: #If user input is not a number
        print("Invalid input")
        break