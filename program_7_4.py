"""Task 4. Implement a script which returns the longest word in the given
string.

The word can contain any symbols except whitespaces ( , \n, \t and so on).

If there are multiple longest words in the string with a same length
return the word that occurs first.
"""
def get_longest_word(s: str) -> str:
    longest_word = ''

    for word in s.split():
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word

s = input('Введіть послідовність слів: ')
print(f'Найдовше слово: {get_longest_word(s)}')
