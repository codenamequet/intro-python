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

hey_bob(s)
