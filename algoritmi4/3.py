def count_chars(string):
    char_counts = {}
    for char in string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    for char, count in char_counts.items():
        print(f"{char}: {count}")

# Пример использования:
count_chars("hello world")
