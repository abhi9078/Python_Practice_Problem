def balanced_paren(inp_str):
    my_list = []
    list1 = ['(', '[', '{']
    list2 = [')', ']', '}']

    for c in inp_str:
        if c in list1:
            my_list.append(c)
        elif c in list2:
            i = list2.index(c)
            if len(my_list) > 0 and list1[i] == my_list[len(my_list)-1]:
                my_list.pop()
            else:
                return "Not balanced paren"
    if len(my_list) == 0:
        return "Balanced Paren"
    else:
        return "Unbalanced"


if __name__ == "__main__":
    str_in = input("Enter a parenthesis operation")
    output = balanced_paren(str_in)
    print(output)
