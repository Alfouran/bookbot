def main():
    with open("books/frankenstein.txt") as f:

        file_contents = f.read()

        return file_contents

#main()

def count_words(str):
    return len(str.split())

#count_words(main())
    
def count_letters(str):
    str = str.lower()
    str_dict = {}
    for i in str:
        if i.isalpha():
            if i in str_dict:
                str_dict[i] += 1
            else:
                str_dict[i] = 1
    list_dict = list(str_dict.items())
    print("--- Begin report of books/frankenstein.txt ---")
    print(count_words(str), "words found in the document")
    print("\n")
    for p in list_dict:
        print(f"The '{p[0]}' character was found {p[1]} times")
    print("--- End report ---")
    return ""
    
    

print(count_letters(main()))





