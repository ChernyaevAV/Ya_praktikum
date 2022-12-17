def is_sub_sequence(sub_text, text):
    len_sub_text = len(sub_text)
    len_text = len(text)
    index_sub_text = 0
    index_text = 0
    while index_sub_text < len_sub_text and index_text < len_text:
        if sub_text[index_sub_text] == text[index_text]:
            index_sub_text += 1
        index_text += 1
    return index_sub_text == len_sub_text


def main():
    sub_text = input()
    text = input()
    print(is_sub_sequence(sub_text, text))


if __name__ == '__main__':
    main()
