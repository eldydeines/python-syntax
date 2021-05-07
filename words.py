def print_upper_words1(words):
    """Converting words to uppercase and printing"""

    for word in words:
        print(word.upper())

def print_upper_words2(words):
    """Converts only words that start with E and prints those words only """

    for word in words:
        if word[0] == 'e' or word[0] == 'E':
            print(word.upper())

def print_upper_words3(words,letters):
    """Converts only words that match letters and prints those words only """

    for word in words:
        for letter in letters:
          if word[0] == letter or word[0] == letter:
            print(word.upper())  


words = ["hello", "echo", "ask", "five","yoo-hoo","every"]
letters = ["h" , "f"]

# Test run 1
print("Output of Words1")
print_upper_words1(words)

# Test run 2
print("Output of Words2")
print_upper_words2(words)

# Test run 3
print("Output of Words3")
print_upper_words3(words, letters)