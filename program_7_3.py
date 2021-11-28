"""Task 3. Implement a script which works the same as str.split
Note: Usage of str.split method is prohibited
"""

def split(s: str, sep: str) -> list:
    parts = []

    while True:
        if sep not in s:
            parts.append(s)
            break

        sep_ind = s.index(sep)
        parts.append(s[:sep_ind])
        s = s[sep_ind + len(sep):]

    return parts

s = input('Введіть послідовність символів: ')
sep = input('Введіть сераратор: ')

print('Результат роботи функції split():' )
print(split(s, sep))
