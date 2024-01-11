import sys
from os.path import join, dirname

sys.path.append(join(dirname(__file__), "..", ""))
from API import lms
from API.role import add_role_to_course

list_course = []
school = lms.New(dmn="xanhsm", user_code="gsm")

for c in list_course:
    add_role_to_course(school, iid_course=c["iid"], iid_role=56988217)
