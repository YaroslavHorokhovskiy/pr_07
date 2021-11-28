"""Task 2. Write a script that checks whether a string is a palindrome or not.
Returns 'True' if it is palindrome, else 'False'.

To check your implementation you can use strings from here
(https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes).

The script has to ignore special characters, whitespaces and different cases.
"""
def is_palindrome(s: str) -> bool:
    # Формуємо рядок тільки з літер алфавиту та цифр
    clean_str = ''
    for char in s.lower():
        if char.isalnum():
            clean_str += char

    return True if clean_str == clean_str[::-1] else False

s = input('Введіть яку-небудь фразу: ')

if is_palindrome(s):
    print('Фраза є паліндромом.')
else:
    print('Фраза не є паліндромом.')
