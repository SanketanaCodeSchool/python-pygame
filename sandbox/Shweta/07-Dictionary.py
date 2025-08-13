'''
Write a function that counts how many times each vowel appears in a given string and stores the result in a dictionary.
Example Input:
text = "hello world"
Expected Output:
{"a": 0, "e": 1, "i": 0, "o": 2, "u": 0}

'''

vowels_count = {}

text = input("Enter the sentence: ")
vowel = 'aeiou'

for i in text:
    if i in vowel:
        if i in vowels_count:
            vowels_count[i] = vowels_count[i]+1
        else:
            vowels_count[i]=1

print(vowels_count)
