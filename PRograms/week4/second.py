"""Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program."""
def get_word():
    word=input("enter the word: ")
    return word
word=get_word()
def count_letters(word):
    upper=0
    lower=0
    for char in word:
        if char.isupper():
            upper +=1
        elif char.islower():
            lower +=1
    return upper,lower
upper,lower=count_letters(word)
print(f"the number of uppercase letter is {upper} and lowercase letter is {lower}")

