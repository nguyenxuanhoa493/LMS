import subprocess, os, urllib, platform, time, json, random, re
import logging as log


def loging(*data):
    log.basicConfig(filename="./log/debug.log", level=log.DEBUG)
    for item in data:
        log.debug(item)


def get_ts_now():
    return int(time.time())


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


def save_file(url_file, folder_path, file_name):
    path_file = os.path.join(folder_path, file_name)
    if not os.path.exists(path_file):
        # Lưu file về và mở folder_path
        urllib.request.urlretrieve(
            url_file,
            path_file,
        )
        print(f"Đã tải file {file_name}")
        time.sleep(random.randint(1, 3))
    else:
        print(f"{file_name} đã tồn tại")


def get_full_path(folder_path, sub_path):
    return os.path.join(folder_path, sub_path)


def load_json(path_file):
    with open(path_file, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(path_file, data):
    with open(path_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def append_json(path_file, new_data, mode="extend"):
    # mode extent or append
    try:
        data = load_json(path_file)
    except:
        data = []
    if mode == "append":
        data.append(new_data)
    else:
        data.extend(new_data)
    save_json(path_file, data)


def check_and_create_subdirectory(parent_directory_path, subdirectory_name):
    parent_directory_path = str(parent_directory_path)
    subdirectory_name = str(subdirectory_name)
    if os.path.exists(parent_directory_path):
        subdirectory_path = os.path.join(parent_directory_path, subdirectory_name)
        # Check if the subdirectory exists
        if not os.path.exists(subdirectory_path):
            try:
                # If it doesn't exist, create the subdirectory
                os.makedirs(subdirectory_path)
                print(
                    f"Đã tạo thư mục '{subdirectory_name}' trong '{parent_directory_path}'."
                )
            except Exception as e:
                print(f"Error: {e}")
        return subdirectory_path
    else:
        print(f"{parent_directory_path} không tồn tại")


def find_and_move_top(arr, key):
    try:
        index_of_number = arr.index(key)
        arr.insert(0, arr.pop(index_of_number))
    except ValueError:
        print(f"Số {key} không tồn tại trong danh sách.")
    return arr


def add_url_to_ts_files(m3u8_content, base_url):
    # Tìm tất cả các đường dẫn tới các file ts trong nội dung m3u8
    ts_files = re.findall(r"#EXTINF:[\d.]+,\n(.*\.ts)", m3u8_content)

    # Thêm base_url vào từng đường dẫn ts
    updated_ts_files = [f"{base_url}/{file}" for file in ts_files]

    # Thay thế các đường dẫn ts cũ trong nội dung m3u8 bằng các đường dẫn mới
    for i, old_ts_file in enumerate(ts_files):
        m3u8_content = m3u8_content.replace(old_ts_file, updated_ts_files[i])

    return m3u8_content


def get_type_of_file_from_file_name(file_name):
    # Tách phần mở rộng của tên file
    match = re.search(r"\.([a-zA-Z0-9]+)$", file_name)
    if match:
        return "audio" if match.group(1) == "mp3" else "video"
    else:
        return None


def merge_json_in_folder(path_folder, path_output_file):
    files = [f for f in os.listdir(path_folder) if f.endswith(".json")]
    result = []
    for file_name in files:
        path_file = os.path.join(path_folder, file_name)
        result.extend(load_json(path_file))
    save_json(path_output_file, result)
