import sys
from os.path import join, dirname
from random import randint

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms

school = lms.New(dmn="xanhsm", user_code="gsm")
list_course = [
    {"iid": 13288744, "id": "65828a78f253ce272704577e", "name": "Giới thiệu về Vieted"},
]
user_code = "nv02"
for c in list_course:
    # auto learn
    course_temp = school.course(iid_course=c["iid"], load_data=True)
    if user_code:
        course_temp.auto_learn(user_code)
        continue
    for u in course_temp.users:
        course_temp.auto_learn(
            user_code=u["code"],
            progress_min=50,
            progress_max=100,
            spent_time_min=300,
            spent_time_max=1200,
        )
    course_temp.resync_score()
