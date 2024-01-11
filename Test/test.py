import re

# Chuỗi văn bản chứa từ khoá trong dấu ngoặc đơn
text = "Tạo khoá học (Tạo khoá học) là quan trọng."

# Biểu thức chính quy để tìm từ khoá trong dấu ngoặc đơn
pattern = r"\((.*?)\)"

# Sử dụng re.findall để tìm tất cả các kết quả phù hợp
matches = re.findall(pattern, text)

# In ra kết quả
print(matches[0])
