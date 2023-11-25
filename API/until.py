def get_value_of_index_in_list(input_list: list, index: int, default=False):
    """
    Lấy giá trị thứ index trong mảng input_list.
    Nếu không có thì sẽ trả về:
    - False nếu không có default
    - default nếu có default

    """
    try:
        return input_list[index]
    except IndexError:
        return default if default else False
