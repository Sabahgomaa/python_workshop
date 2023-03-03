# # 1/ What is 7 to the power of 4?
# var = 7 ** 4
# print(var)
#
# # 2/ Split this string
# # s = "Hi there Sam!"
# s = 'Hi there Sam!'
# print(s.split())
#
# # 3/ Given the variables:
# # planet = "Earth" diameter = 12742
# # Use .format() to print the following string:
# # The diameter of Earth is 12742 kilometers.
# planet = "Earth"
# diameter = 12742
# print("The diameter of {} is {} kilometers.".format(planet, diameter))
#
# # 4/ Given this nested list, use indexing to grab the word "hello"
# lst = [1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
# var = lst[3][1][2][0]
# print(var)
#
# # 5/ Given this nest dictionary grab the word "hello". Be prepared, this will be annoying/tricky
# d = {'k1': [1, 2, 3, {'tricky': ['oh', 'man', 'inception', {'target': [1, 2, 3, 'hello']}]}]}
# var = d['k1'][3]['tricky'][3]['target'][3]
# print(var)


# 6/ What is the main difference between a tuple and a list?
def domainGet(email):
    return email.split('@')[-1]


print(domainGet('user@domain.com'))


# 7/ Create a basic function that returns True if the word 'dog' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def findDog(st):
    return 'dog' in st.lower().split()


print(findDog('Is there a dog here?'))


# 8/ Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.
def countDog(st):
    count = 0
    for word in st.lower().split():
        if word == 'dog':
            count += 1
    return count


print(
    countDog('This dog runs faster than the other dog dude!'))

# 9/Use lambda expressions and the filter() function to filter out words
# from a list that don't start with the letter 's'. For example:

seq = ['soup', 'dog', 'salad', 'cat', 'great']
print(list(filter(lambda word: word[0] == 's', seq)))
