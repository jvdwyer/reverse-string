def reverse_string(word):
    index = len(word)
    reversed_string = [str]*index
    for c in word:
        reversed_string[index - 1] = c
        index -= 1
    return ''.join(reversed_string)
