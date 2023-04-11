def encrypt_caesar(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # определяем номер символа в алфавите
            char_code = ord(char.lower()) - ord('a')
            # сдвигаем символ по алфавиту на ключ
            shifted_code = (char_code + key) % 26
            # определяем новый символ на основе сдвинутого номера
            new_char_code = shifted_code + ord('a')
            new_char = chr(new_char_code)
            # сохраняем новый символ в зашифрованном тексте
            if char.isupper():
                new_char = new_char.upper()
            encrypted_text += new_char
        else:
            # сохраняем не-буквенный символ в зашифрованном тексте
            encrypted_text += char
    return encrypted_text
text = "Hello, World!"
key = 1
encrypted_text = encrypt_caesar(text, key)
print(encrypted_text)  
