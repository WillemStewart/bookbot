from stats import get_num_words

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_txt(book_path)
    words = get_num_words(text)
    ctrcount = count_characters(text)
    print("--- Beginning book analysis ---")
    print("\n")
    print(f"There are {words} words found in the document")
    print("\n")
    character_report(ctrcount)
    print("\n")
    print("--- End of book analysis ---")


def count_characters(txt):
    strint = {}
    compare = ord('a')
    ctr = 0
    newtxt = txt.lower()
    while compare < 123:
        temp = chr(compare)
        ctr = newtxt.count(temp)
        strint[temp] = ctr
        compare += 1
        ctr = 0
    
    return strint

def get_book_txt(path):
    with open(path) as f:
        return f.read()

def sort_on(d):
    return d["num"]

def character_report(dictionary):
    sorted_list = []
    for chars in dictionary:
        sorted_list.append({"char" : chars, "num" : dictionary[chars]})
    sorted_list.sort(reverse = True, key = sort_on)
    for i in range(len(sorted_list)):
        letter = sorted_list[i]['char']
        number = sorted_list[i]['num']
        print(f"The '{letter}' character was found {number} times")
main()