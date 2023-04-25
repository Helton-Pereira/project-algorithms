def merge_sort(word):
    if len(word) <= 1:
        return word

    mid = len(word) // 2
    left, right = merge_sort(word[:mid]), merge_sort(word[mid:])
    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result += left
    result += right

    return result


def is_anagram(first_string, second_string):
    word1 = first_string.lower()
    word2 = second_string.lower()

    sorted_word1 = merge_sort(word1)
    sorted_word2 = merge_sort(word2)

    if not first_string or not second_string:
        return ("".join(sorted_word1), "".join(sorted_word2), False)
    return (
        "".join(sorted_word1),
        "".join(sorted_word2),
        sorted_word1 == sorted_word2
    )
