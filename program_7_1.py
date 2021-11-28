"""Task 1. Implement a script which receives a string and replaces
all " symbols with ' and vise versa. The script should return modified string.
"""

def get_modified_str(s: str) -> str:
    s_parts = s.split('"') # Розбивка по символу "

    for i, part in enumerate(s_parts):
        s_parts[i] = part.replace("'", '"') # Заміна ' на "

    return "'".join(s_parts) # З'єднання символом '

s = input('Введіть будь-яку послідовність символів: ')
print(f'Модіфікована послідовність символів: {get_modified_str(s)}')
