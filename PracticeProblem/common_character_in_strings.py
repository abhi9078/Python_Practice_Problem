def common_char(f_str, s_str):
    common = set(f_str).intersection(s_str)
    out_string = ''.join(common)
    return out_string


if __name__ == "__main__":
    str1 = "hello"
    str2 = "world"
    print(common_char(str1, str2))
