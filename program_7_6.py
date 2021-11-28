"""Task 6. Create a script that for a positive integer n calculates the result
value, which is equal to the sum of the '1' in the binary representation of n
otherwise, returns None.

Example:
    n = 14 = 1110 result = 3
    n = 128 = 10000000 result = 1
"""

def get_bits_sum(n: int) -> int:
    bits_sum = 0

    # Перші два символи обрізаємо, бо там сигнатура бінарного формату (0b)
    # (хоча це і необов'язково для поточної задачі)
    bits = bin(n)[2:]

    for bit in bits:
        if bit == '1':
            bits_sum += 1

    return bits_sum

n = int(input('Введіть будь-яке ціле позитивне число: '))
print(f'Число у бінарному форматі: {bin(n)}')
print(f'Сума одиниць в бінарному вигляді: {get_bits_sum(n)}')
