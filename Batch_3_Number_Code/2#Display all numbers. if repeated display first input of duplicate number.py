filtered_numbers = []  # Initialize an empty list to store unique occurrences
for _ in range(10):  # Repeat process for 10 independent inputs
    num = int(input("Enter a number: "))  # Get user input
    if num not in filtered_numbers:  # Check if the number is already in filtered_numbers
        filtered_numbers.append(num)  # If not, add it to the list
print("Filtered numbers:", filtered_numbers)  # Print the final filtered list