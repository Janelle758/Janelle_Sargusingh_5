my_str = "The quick brown fox jumps over the lazy dog"

# a. Print the string to the page
print(my_str)

# b. Print the length of the string to the page
print(len(my_str))

# c. Print the string in all uppercase letters
print(my_str.upper())

# d. Print the string in all lowercase letters
print(my_str.lower())

# e. Print the string in title case
print(my_str.title())

# f. Print the string in reverse
print(my_str[::-1])

# g. Print the string in reverse title case
print(my_str[::-1].title())

# h. Count the number of times the letter “a” appears in the string
print(my_str.count('a'))

# i. Count the number of times the word “the” appears in the string
print(my_str.count('the'))

# j. Replace the word “the” with the word “a”
print(my_str.replace('the', 'a'))


my_str = "The quick brown fox jumps over the lazy dog"
frequency_dict = {}

for char in my_str:
    if char.isalpha():
        char = char.lower()
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

print(frequency_dict)


people = ['Jane', 'John', 'Jack', 'Janet']
sex = ['Female', 'Male', 'Male', 'Female']
age = [23, 34, 16, 28]

# Interpolate the three lists into a string
for i in range(len(people)):
    print(f"{people[i]} the {sex[i]} is {age[i]} years old.")
