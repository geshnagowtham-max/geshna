def analyze_text(text):
    sentences = text.count('.') + text.count('!') + text.count('?')
    words = text.split()
    num_words = len(words)
    num_chars = len(text)
    print("Text Analysis:")
    print("Total sentences:", sentences)
    print("Total words:", num_words)
    print("Total characters:", num_chars)

def count_keyword(text, keyword):
    # Case-insensitive keyword counting
    words = text.lower().split()
    count = words.count(keyword.lower())
    print(f"The word '{keyword}' appears {count} times in the text.")

# Main logic
text = input("Enter the text for analysis:\n")
analyze_text(text)
keyword = input("Enter the keyword to count: ")
count_keyword(text, keyword)
