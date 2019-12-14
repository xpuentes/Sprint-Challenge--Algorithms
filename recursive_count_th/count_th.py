'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word_len = len(word)

    if word_len < 2:
        return 0

    if word[:2] == 'th':
        return count_th(word[1:]) + 1

    return count_th(word[1:])

print(count_th('ththasdfasthelakwjeroithlkajsdfthe'))