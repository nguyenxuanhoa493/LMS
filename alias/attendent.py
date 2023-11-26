import sys, os, re

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ""))
from API import lms
from API.until import get_value
from API.course import get_list_course_of_ep
from API.course import New as Newcourse

# truyền vào dmn và  ds link import điểm danh
dmn = sys.argv[1]
list_iid = sys.argv[2].split(",")
type_target = get_value(sys.argv, key=3, default="course")
school = lms.New(dmn=dmn)
if type_target == "ep":
    list_target = [get_list_course_of_ep(school, iid_ep) for iid_ep in list_iid]
    list_target = [item["iid"] for sublist in list_target for item in sublist]
else:
    list_target = list_iid

for iid_course in list_target:
    course_temp = Newcourse(school, iid_course)
    course_temp.attentdent_all()
