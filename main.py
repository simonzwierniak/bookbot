def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

if __name__ == "__main__":
    main()

def count_words(text):
    words = text.split()
    return len(words)

with open("books/frankenstein.txt") as f:
    text = f.read()
    words = count_words(text)
    print(words)