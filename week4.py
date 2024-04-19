msg = str(input("Enter your message: "))
count = 0
for i in msg:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        count += 1
        print(count)

# Function for use: This script counts the number of vowels (a, e, i, o, u) in a given message and prints the count for each vowel encountered.
