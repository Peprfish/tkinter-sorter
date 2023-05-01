from random import shuffle

class SortObject:
    def __init__(self, name, root, is_root):
        # name is the string the SortObject instance represents
        # root is a pointer to the root SortObject, representing the first string in to_sort
        self.name = name

        self.left_child = None
        self.right_child = None

        if not is_root:
            cp = root # 'cp' stands for 'candidate parent'
            cphecs = False # 'cphec' stands for 'candidate parent has empty child slot'
            
            while not cphecs:
                adoption_response = cp.comp_and_ret_availability(self)
                if not adoption_response[0]: # activates if candidate parent has no empty child slot
                    cp = adoption_response[1] # take the SortObject in that child slot as cp, and repeat process
                else:
                    cphecs = True
            
            self.parent = cp
        else:
            self.parent = None
    
    def comp_and_ret_availability(self, cc): # 'cc' stands for 'candidate child'
        # UI block
        print(f"[0]: {self.name}")
        print(f"[1]: {cc.name}")
        res = int(input("Which goes first, [0] or [1]? (Type '0' or '1' and press enter): "))
        # End of UI block
        if res == 1:
            if self.left_child == None:
                self.left_child = cc # adoption successful
                return [True, None]
            else:
                return [False, self.left_child]
        else:
            if self.right_child == None:
                self.right_child = cc # adoption successful
                return [True, None]
            else:
                return [False, self.right_child]

    def expression(self, list_sorted): # LNR traversal by recursively adding to list
        if self.left_child != None:
            list_sorted = self.left_child.expression(list_sorted)
        list_sorted.append(self.name)
        if self.right_child != None:
            list_sorted = self.right_child.expression(list_sorted)
        return list_sorted

def main():
    # obtain a list of strings to sort from the user
    # UI Block
    to_sort_unshuffled = []
    res = input("Add a word or phrase that you want to sort, or simply press enter to stop adding: ")
    while res != "":
        to_sort_unshuffled.append(res)
        res = input("Add a word or phrase that you want to sort, or simply press enter to stop adding: ")
    shuffle(to_sort_unshuffled)
    to_sort = to_sort_unshuffled.copy()
    # End of UI block

    # create an ecosystem of SortObjects
    string_count = len(to_sort)
    all_strings = [None for _ in range(string_count)]
    root_string = all_strings[0] = SortObject(to_sort[0], None, True)
    for i in range(1, string_count):
        all_strings[i] = SortObject(to_sort[i], root_string, False)

    # output!
    print(root_string.expression([]))

if __name__ == "__main__":
    main()