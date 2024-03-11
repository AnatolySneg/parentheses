def get_invalid_indexes(data: list, char: tuple[str]) -> list[int]:
    count = 0
    data_index = []
    for i in data:
        start_index = data.index(i, count)
        data_index.append([i, data.index(i, count)])
        count += 1

    return [i[1] for i in data_index if i[0] in char]


def is_valid_parentheses(data: str, parentheses_char: tuple[str] = ("(", ")", "[", "]", "{", "}")) -> bool | list[int]:
    """
    function gets string with or without parentheses
    :returns: 'True' if parentheses are closable;
    :returns: 'False' if there is no parentheses in string;
    :returns: 'list[int]' of indexes of invalid parentheses otherwise.
    """
    list_data = list(data)
    list_parentheses = list(filter((lambda i: i in parentheses_char), list_data))
    income_len = len(list_parentheses)

    if not list_parentheses:
        return False

    if income_len % 2:
        return get_invalid_indexes(list_data, parentheses_char)

    string_parentheses = "".join(list_parentheses)

    while income_len != 0:
        string_parentheses = string_parentheses.replace("()", "")
        string_parentheses = string_parentheses.replace("[]", "")
        string_parentheses = string_parentheses.replace("{}", "")
        output_len = len(string_parentheses)
        if income_len == output_len:
            return get_invalid_indexes(list_data, parentheses_char)
        income_len = output_len

    return not string_parentheses
