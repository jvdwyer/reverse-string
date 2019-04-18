def reverse_string(word):
    index = len(word)
    reversedString = [str]*index
    for c in word:
        reversedString[index - 1] = c
        index -= 1
    return ''.join(reversedString)

reverse_string('hello')