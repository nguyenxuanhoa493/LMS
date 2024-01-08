import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms
from API.session import attendance_one_user


school = lms.New(dmn="bvl")

iid_course = 13017679
data = school.course(iid_course=iid_course, load_data=True)
checked = """D1077A3HRV
D1077A3HRY""".replace(
    "\n", " "
).split(
    " "
)
print(checked)

for sesion in data.sessions:
    for user in data.users:
        # nếu ds user rỗng hoặc có và u.code trong list đó thì đc điểm danh
        if (checked[0] == "") or (checked[0] != "" and (user["code"] in checked)):
            attendance_one_user(school, iid_course, sesion, user, status=1)
