def first_non_repeating_char(s):
    char_dict = {}
    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] = char_dict.get(char)+1
    
    for key,value in char_dict.items():
        if value > 1:
            continue
        else:
            return s.find(key) 

    return -1


if __name__ == "__main__":
    print(first_non_repeating_char(s="abcdcafbd"))