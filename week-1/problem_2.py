# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 

# s = 'azcbobobegghakl'
s = 'aqbobboboobobbbobobboobfobobobboboboboboobobbsbobbobobool'

#turn string into an array 
#if i == b go to the next index if it == o do the same and if that index == b increase counter by 1
#if the next index after the second b is an o repeat process
# elsif i !==b continue to the next letter

def hey_bob(string):
    count = 0
    for i in range(len(string)):
        if(string[i:i + 3] == 'bob'):
            count += 1
    # print(f'Number of times bob occurs is: {count}')
    print('Number of times bob occurs is: ' + str(count))

# def hey_bob(string):
#     count = 0
#     for i in range(len(string)):
#         if(string[i:i + 3] == 'bob'):
#             count += 1
#     print('Number of times bob occurs is: ' + str(count)

# def hey_bob(string):
#     count = string.count('bob')
#     if count > 0:
#         print(f'bob is here {count} times')

# def hey_bob(string):
#     count = 0
#     for i in range(len(string)):
#         # print(f'{string[i]}')
#         if (string[i] == 'b'):
#             print(f'the first joint {string[i]}')
#             if (int(string[i + 1]) <= len(string) and string[i + 1] == 'o'):
#                 print(f'the second joint {string[i + 1]}')
#                 if (i + 2 <= len(string) and string[i + 2] == 'b'):
#                     print(f'the third joint {string[i + 2]}')  
#                     count += 1
#     print(f'the count is {count}')


hey_bob(s)
