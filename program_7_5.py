"""Task 5. For a positive integer n calculate the result value, which is equal
to the sum of the odd numbers of n.

Example:
    n = 1234 result = 4
    n = 246 result = 0
"""
def get_odd_digits_sum(n: int) -> int:
    digits_sum = 0

    for char in str(n):
        digit = int(char)
        if digit % 2 != 0:
            digits_sum += digit

    return digits_sum

n = int(input('Введіть будь-яке ціле позитивне число: '))
print(f'Сума непарних цифр числа: {get_odd_digits_sum(n)}')
