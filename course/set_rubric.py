import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.course import set_rubric

school = lms.New(dmn="xanhsm")
list_course = [
    {"iid": 13101895, "id": "65828a78f253ce272704577e", "name": "Giới thiệu về Vieted"},
    {
        "iid": 13101886,
        "id": "65828a50efad3b2f5c0d10d8",
        "name": "Phương pháp huấn luyện nhân viên hiệu quả",
    },
    {
        "iid": 13101880,
        "id": "65828a50efad3b2f5c0d10d3",
        "name": "Phương pháp tạo động lực làm việc cho nhân viên",
    },
    {
        "iid": 13101875,
        "id": "65828a50efad3b2f5c0d10ce",
        "name": "Kỹ năng quản lý và giải quyết xung đột",
    },
    {
        "iid": 13101365,
        "id": "65826ffaa7ee29d0170853d2",
        "name": "Kỹ năng ủy thác công việc",
    },
    {"iid": 13101360, "id": "65826ffaa7ee29d0170853cd", "name": "Kỹ năng giao tiếp"},
    {
        "iid": 13101355,
        "id": "65826ffaa7ee29d0170853c8",
        "name": "5 tư duy cần có thời 4.0",
    },
    {
        "iid": 13101283,
        "id": "65826c23c9ce637d3f00f3de",
        "name": "Bí quyết tăng doanh số thông qua dịch vụ khách hàng",
    },
    {
        "iid": 13101278,
        "id": "65826c22c9ce637d3f00f3d9",
        "name": "Sử dụng trí tuệ cảm xúc trong công việc",
    },
    {
        "iid": 13101272,
        "id": "65826c22c9ce637d3f00f3d3",
        "name": "Giải quyết vấn đề một cách logic",
    },
]
for c in list_course:
    set_rubric(school, c, 13101250)
