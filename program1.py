#Easy 1
#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal 
#substring consisting of non-space characters only.

def length_of_last_word(s):
    # Split the string into words
    words = s.split()

    # Check if there are any words
    if not words:
        return 0

    # Return the length of the last word
    return len(words[-1])
s=input("enter string")
print(length_of_last_word(s))
