# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world



str = input("Enter whitespace separated sequence of words: ")

words = str.split(" ")        # Split the string to get individual words in list.


setOfWord = set(words)        # convert list to set to remove duplicated words

listOfUniqueWords = list(setOfWord)  # convert set to list of unique words    



sortedListOfUniqueWords = sorted(listOfUniqueWords)        # sort the unique word list


listToString = " ".join(sortedListOfUniqueWords)           # convert list to string
print(listToString)
