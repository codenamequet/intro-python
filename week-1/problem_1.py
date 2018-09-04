# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 

# s = 'azcbobobegghakl'
s = 'vkssemiihazwvepyblyx'

def count_vowels(string):
    vowels = 0
    for i in string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels += 1
    # print ('Number of vowels: ' + str(vowels))
    print (f'Number of vowels: {vowels}')

count_vowels(s)
