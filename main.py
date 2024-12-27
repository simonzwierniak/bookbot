def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = count_words(text)
        lower_words = get_lower_words(text)
        char_count = get_char_count(lower_words)
        report = get_report(words, char_count)
        print(report)

def count_words(text):
    words = text.split()
    return len(words)

def get_lower_words(text):
    lower_words = text.lower()
    return lower_words

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def get_report(words, char_count):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{words} words found in the document"
    for char, count in char_count.items():
        report += f"The '{char}' character was found {count} times\n"
    report += "--- End report ---"
    return report

if __name__ == "__main__":
    main()