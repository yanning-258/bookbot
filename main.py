def get_file(book_path):
    with open(book_path) as f:
        file = f.read()
    return file

def count_num_char(text):
    text_s = text.split()
    return len(text_s)

def get_char_dict(text):
    char = {}
    for c in text:
        lowered = c.lower()
        if lowered in char:
            char[lowered] += 1
        else:
            char[lowered] = 1
    return char



def get_list(char_dict):
    list_of_dict = []
    item = {}
    
    for pair in char_dict:
        item = {"char": pair, "num":char_dict[pair]}
        list_of_dict.append(item)

    def sort_on(dict):
        return dict["num"]

    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def print_report(num_words, list_of_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")

    for item in list_of_dict:
        if item["char"].isalpha() == False:
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def main():
    text = get_file("books/frankenstein.txt")
    num_words = count_num_char(text)
    char_dict = get_char_dict(text)
    list_of_dict = get_list(char_dict)
    #print(list_of_dict)
    print_report(num_words, list_of_dict)
    



main()