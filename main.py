def main():
    with open("books/frankenstein.txt") as f:
        text = f.read()
        words = count_words(text)
        lower_words = get_lower_words(text)
        print(words)
        print(lower_words)

def count_words(text):
    words = text.split()
    return len(words)

def get_lower_words(text):
    lower_words = text.lower()
    return lower_words

if __name__ == "__main__":
    main()