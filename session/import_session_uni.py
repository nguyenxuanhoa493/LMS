import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms


def import_session(course, data):
    temp_course = school.course(iid_course=course["iid"])
    teacher_master = course["teacher_master"]
    for session in data:
        session["teacher"] += teacher_master
        temp_course.add_new_a_session(session)

    list_teacher = teacher_master
    for session in data:
        list_teacher += session["teacher"]
    temp_course.add_teacher_to_course(set(list_teacher))


list_course = {
    "k113": {"iid": 2008185, "teacher_master": [267518]},
    "k112": {"iid": 2008158, "teacher_master": [267517]},
    "k116": {"iid": 2020015, "teacher_master": [267509]},
    "k5": {"iid": 2009051, "teacher_master": [267497]},
    "k7": {"iid": 2027022, "teacher_master": [267497]},
    "2025939": {"iid": 2025939, "teacher_master": [284058]},
}

data = [
    {
        "name": "Chuyên đề 5: Kỹ năng tổ chức, điều hành họp",
        "date": "2024-1-10",
        "time": "Tối",
        "teacher": [267495],
    },
    {"name": "Thảo luận CĐ5", "date": "2024-1-11", "time": "Tối", "teacher": [267495]},
    {
        "name": "Chuyên đề 6: Kỹ năng đánh giá thực thi công vụ",
        "date": "2024-1-12",
        "time": "Tối",
        "teacher": [267497],
    },
    {"name": "Thảo luận CĐ6", "date": "2024-1-13", "time": "Tối", "teacher": [267497]},
    {
        "name": "Chuyên đề 4: Kỹ năng áp dụng pháp luật",
        "date": "2024-1-14",
        "time": "Tối",
        "teacher": [267499],
    },
]
school = lms.New(dmn="hth", type_dmn="uni")
# import_session(list_course["k7"], data)
