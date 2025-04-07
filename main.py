import string

def count_words(text):
    """Counts the number of words in a given text."""
    words = text.split()
    return len(words)

def count_characters(text):
    """Counts the number of characters in a given text, excluding spaces."""
    return len(text.replace(" ", ""))

def count_sentences(text):
    """Counts the number of sentences in a given text."""
    sentences = text.split('.')
    return len([s for s in sentences if s.strip()])

def main():
    print("Advanced Word Counter Program")
    print("--------------------------------")
    
    # Taking user input
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    
    # Counting words, characters, and sentences
    word_count = count_words(user_input)
    char_count = count_characters(user_input)
    sentence_count = count_sentences(user_input)
    
    # Displaying output
    print("\nText Analysis:")
    print(f"- Word Count: {word_count}")
    print(f"- Character Count (excluding spaces): {char_count}")
    print(f"- Sentence Count: {sentence_count}")

if __name__ == "__main__":
    main()
