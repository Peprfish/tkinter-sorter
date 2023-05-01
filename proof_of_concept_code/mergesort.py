from random import shuffle

def split_and_recombine(content_list):
    list_length = len(content_list)
    if list_length == 1:
        return content_list
    else:
        # split into two
        child_list_unsorted_a = content_list[0:list_length // 2]
        child_list_unsorted_b = content_list[list_length // 2:list_length]
        
        # recursive step, obviously
        child_list_sorted_a = split_and_recombine(child_list_unsorted_a)
        child_list_sorted_b = split_and_recombine(child_list_unsorted_b)

        output_list = []

        # flags representing whether either sorted component has been fully 'unloaded'
        # when this occurs, we obviously just append the rest of the other component to our output_list
        # this takes place at [BOOKMARK1]
        a_empty = False
        b_empty = False

        while not (a_empty or b_empty):
            # UI block
            print(f"[0]: {child_list_sorted_a[0]}")
            print(f"[1]: {child_list_sorted_b[0]}")
            res = int(input("Which goes first, [0] or [1]? (Type '0' or '1' and press enter): "))
            # End of UI block

            if res == 0:
                output_list.append(child_list_sorted_a.pop(0))
            else:
                output_list.append(child_list_sorted_b.pop(0))

            a_empty = len(child_list_sorted_a) == 0
            b_empty = len(child_list_sorted_b) == 0

        # [BOOKMARK1]
        if a_empty:
            output_list.extend(child_list_sorted_b)
        else:
            output_list.extend(child_list_sorted_a)

        return output_list

def main():
    # obtain a list of strings to sort from the user
    to_sort = []
    res = input("Add a word or phrase that you want to sort, or simply press enter to stop adding: ")
    while res != "":
        to_sort.append(res)
        res = input("Add a word or phrase that you want to sort, or simply press enter to stop adding: ")
    shuffle(to_sort)

    sorted = split_and_recombine(to_sort)
    print(sorted)

if __name__ == "__main__":
    main()