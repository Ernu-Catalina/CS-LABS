from Count_Letters import count_letters

alphabet_by_frequency = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z']

input_string = input("Enter a message: ")
message = input_string
sorted_message = count_letters(input_string)

result = sorted_message
print()
print(result)