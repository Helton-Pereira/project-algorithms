def is_palindrome_iterative(word):
    if not word:
        return False

    reverse = word[::-1]

    if word == reverse:
        return True
    return False
