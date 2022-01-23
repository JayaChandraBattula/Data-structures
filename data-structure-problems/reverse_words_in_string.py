
def reverse_words_in_string(string):
    words = []
    is_space = False
    for i in reversed(range(len(string))):
        print(i, string[i])
        if string[i] == " ":
            if not is_space:
                words.append(string[i+1:])
                print(words)
                is_space = True
        elif string[i] != " ":
            is_space = False
    return ",".join(words)

if __name__ == "__main__":
    print(reverse_words_in_string("hi chandra me" ))
