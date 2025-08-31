def word_counter():
    text = input("Enter a string: ")
    words = text.split()  # split text by spaces
    print("Number of words:", len(words))
    print("Number of characters:", len(text))

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1  # count frequency

    print("Word frequencies:")
    for word, count in word_freq.items():
        print(word, ":", count)


word_counter()
