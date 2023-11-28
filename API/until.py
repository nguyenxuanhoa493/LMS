import subprocess, os, urllib, platform


def get_value(input_data, key, default=False):
    """
    Lấy giá trị key trong input_data.
    Nếu không có thì sẽ trả về:
    - False nếu không có default
    - default nếu có default
    """
    try:
        return input_data[key]
    except:
        return default if default else False


def remove_chars(input_string, chars_need_remove):
    # Loại bỏ các ký tự của chars_need_remove trong input_string
    result = ""
    for char in input_string:
        if char not in chars_need_remove:
            result += char
    return result


def clear_file_name(file_name):
    # Loại bỏ các ký tự đặc biệt trong tên file
    invalid_chars = r"<>:\"/\|?*"
    new_name = remove_chars(file_name, invalid_chars)
    new_name = new_name.replace("\t", " ")
    return new_name


def open_folder(folder_path):
    if os.path.exists(folder_path):
        system_platform = platform.system().lower()
        if system_platform == "darwin":
            # macOS
            subprocess.Popen(["open", folder_path])
        elif system_platform == "windows":
            # Windows
            subprocess.Popen(["explorer", folder_path], shell=True)
        else:
            print(f"Hệ điều hành '{system_platform}' không được hỗ trợ.")
    else:
        print(f"Thư mục '{folder_path}' không tồn tại.")


def save_file(url_file, folder_path, fle_name):
    # Lưu file về và mở folder_path
    urllib.request.urlretrieve(
        url_file,
        os.path.join(folder_path, fle_name),
    )


def get_path_full(sub_path):
    return os.path.join(os.path.join(os.path.dirname(__file__), "..", ""), sub_path)
