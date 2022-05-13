def reverse(in_str):
    word = in_str.split(" ")

    lt = [i[::-1] for i in word]

    new_list = " ".join(lt)
    return new_list


if __name__ == "__main__":
    string_input = "hello world"
    output = reverse(string_input)
    print(output)
