with open('text_for_RLE_024.txt', 'w', encoding='UTF-8') as file:
    file.write(input('Какой текст нужно сжать? Напишите: '))
with open('text_for_RLE_024.txt', 'r') as file:
    my_text = file.readline()
    text_compression = my_text.split()

print(my_text)


def rle_encode(text):
    enconding = ''
    prev_char = ''
    count = 1
    if not text:
        return ''

    for char in text:
        if char != prev_char:
            if prev_char:
                enconding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        enconding += str(count) + prev_char
        return enconding


text_compression = rle_encode(my_text)

with open('text_compression_RLE_024.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{text_compression}')
print(text_compression)