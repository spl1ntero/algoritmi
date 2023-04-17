replacement_table = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'H',
    'i': 'I',
    'j': 'J',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'o': 'O',
    'p': 'P',
    'q': 'Q',
    'r': 'R',
    's': 'S',
    't': 'T',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'x': 'X',
    'y': 'Y',
    'z': 'Z'
}

# Получаем текст, который нужно зашифровать
text = input("Введите текст для шифровки: ")

# Проходимся по каждой букве в тексте и заменяем ее на соответствующую букву из таблицы замены
encrypted_text = ""
for letter in text:
    if letter.lower() in replacement_table:
        encrypted_text += replacement_table[letter.lower()]
    else:
        encrypted_text += letter

# Выводим зашифрованный текст
print("Зашифрованный текст: " + encrypted_text)
