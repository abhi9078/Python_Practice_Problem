def balanced_paren(str_in):
    my_dict = {}
    i = 1
    for c in str_in:
        my_dict[i] = c
        i += 1

    last = len(my_dict)
    print(last)
    if my_dict[1] == '(' and my_dict[last] == ')':
        return "Balanced Parenthesis"
    elif my_dict[1] == '[' and my_dict[last] == ']':
        return "Balanced Parenthesis"
    elif my_dict[1] == '{' and my_dict[last] == '}':
        return "Balanced Parenthesis"
    else:
        return "Not balanced Parenthesis"


if __name__ == "__main__":
    inp_str = "(3+2)"
    print(balanced_paren(inp_str))
