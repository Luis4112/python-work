# week 1 and 2, Untitled-1.

# Importing

from datetime import datetime as dt  # importing as alias
import sys  # system functions and parameters.
from datetime import datetime
print("Importing is important")


print(datetime.now())

print(dt.now())


def new_line():
    print('\n')


new_line()

# Advanced Strings
print("Advanced Strings:")
My_name = "Kohta"
print(My_name[0])  # first initial
print(My_name[-1])  # last letter on the string.

sentence = "this is a sentence."

print(sentence[:4])  # first word
# last word, -1 implies removing the period off the sentence
print(sentence[-9:-1])
print(sentence.split())  # split sentence by delimiter(space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))

# quotes inside quotes

quoteception = "I said, 'give me all the money'"

print(quoteception)

quoteception = "I said, \"give me all the money\""
print(quoteception)

print("A" in "Apple")

letter = "a"
word = "Apple"
print(letter.lower() in word.lower())  # improved case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (
    letter.lower() in word_two.lower()))
