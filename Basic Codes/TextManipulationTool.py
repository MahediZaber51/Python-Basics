def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    return len(text)

def count_lines(text):
    lines = text.split('\n')
    return len(lines)

if __name__ == "__main__":
    print("Text Manipulation Tool")
    input_text = input("Enter the text: ")

    word_count = count_words(input_text)
    char_count = count_characters(input_text)
    line_count = count_lines(input_text)

    print("Word Count:", word_count)
    print("Character Count:", char_count)
    print("Line Count:", line_count)
