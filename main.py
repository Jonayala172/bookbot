def main():

    lower_counter = {}
    # Open a file and read its contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(file_contents)

        word_count = count_words(file_contents)
        #print(f"Word count: {word_count}")

        char_list = count_char(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")

    for char in char_list:
        print(f"The '{char['key']}' character was found {char['num']} times")
    
    print("--- End report ---")

def count_words(file_contents):
    # split the file contents into words
    words = file_contents.split()
    return len(words)

def sort_on(lower_counter):
    return lower_counter ["num"]

def count_char(file_contents):
    lower_counter ={}
    # split the file contents into characters
    lower = file_contents.lower()
    for char in lower:
        if char.isalpha():
            if char not in lower_counter:
                lower_counter[char] = 1
            else:
                lower_counter[char] += 1
        else:
            pass

    char_list = []
    for char,count in lower_counter.items():
        char_list.append({"key": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)


    return char_list

        

main()