def get_num_words(fc):
    words = fc.split()
    return len(words)

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

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(dictionary):
    sorted_list = []
    for chars in dictionary:
        sorted_list.append({"char" : chars, "num" : dictionary[chars]})
    sorted_list.sort(reverse = True, key = sort_on)
    return sorted_list