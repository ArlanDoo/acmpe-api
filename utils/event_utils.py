def check_len(elem, length: int, is_max: bool):
    if is_max:
        return len(elem) <= length

    return len(elem) >= length